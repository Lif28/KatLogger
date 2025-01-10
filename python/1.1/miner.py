#A stratum compatible miniminer
#based in the documentation
#https://slushpool.com/help/#!/manual/stratum-protocol
#2017-2019 Martin Nadal https://martinnadal.eu

import socket
import json
import hashlib
import binascii
import time
import random

address = '35NsKJjCCjCZv5FGtuHr3NT7MCMEkYCAxZ'
nonce = hex(random.randint(0, 2**32 - 1))[2:].zfill(8)

host = 'solo.ckpool.org'
port = 3333

#("address:{} nonce:{}".format(address, nonce))
#("host:{} port:{}".format(host, port))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# server connection
sock.sendall(b'{"id": 1, "method": "mining.subscribe", "params": []}\n')
lines = sock.recv(1024).decode().split('\n')
response = json.loads(lines[0])
sub_details, extranonce1, extranonce2_size = response['result']

# authorize workers
sock.sendall(b'{"params": ["' + address.encode() + b'", "password"], "id": 2, "method": "mining.authorize"}\n')

# read until 'mining.notify' is reached
response = b''
while response.count(b'\n') < 4 and not (b'mining.notify' in response):
    response += sock.recv(1024)

# get rid of empty lines
responses = [json.loads(res) for res in response.decode().split('\n') if len(res.strip()) > 0 and 'mining.notify' in res]
p#(responses)

job_id, prevhash, coinb1, coinb2, merkle_branch, version, nbits, ntime, clean_jobs = responses[0]['params']

# target
target = (nbits[2:] + '00' * (int(nbits[:2], 16) - 3)).zfill(64)
#('nbits:{} target:{}\n'.format(nbits, target))

extranonce2 = '00' * extranonce2_size

coinbase = coinb1 + extranonce1 + extranonce2 + coinb2
coinbase_hash_bin = hashlib.sha256(hashlib.sha256(binascii.unhexlify(coinbase)).digest()).digest()

#('coinbase:\n{}\n\ncoinbase hash:{}\n'.format(coinbase, binascii.hexlify(coinbase_hash_bin)))
merkle_root = coinbase_hash_bin
for h in merkle_branch:
    merkle_root = hashlib.sha256(hashlib.sha256(merkle_root + binascii.unhexlify(h)).digest()).digest()

merkle_root = binascii.hexlify(merkle_root).decode()

# little endian
merkle_root = ''.join([merkle_root[i] + merkle_root[i + 1] for i in range(0, len(merkle_root), 2)][::-1])

#('merkle_root:{}\n'.format(merkle_root))

blockheader = version + prevhash + merkle_root + nbits + ntime + nonce + \
              '000000800000000000000000000000000000000000000000000000000000000000000000000000000000000080020000'

# Continuous loop to mine
while True:
    nonce = hex(random.randint(0, 2**32 - 1))[2:].zfill(8)  # Generate a new nonce each time

    # Rebuild blockheader with new nonce
    blockheader = version + prevhash + merkle_root + nbits + ntime + nonce + \
                  '000000800000000000000000000000000000000000000000000000000000000000000000000000000000000080020000'

    # Hash the blockheader
    hash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(blockheader)).digest()).digest()
    hash = binascii.hexlify(hash).decode()
    
    #(f'Attempted hash: {hash}')
    
    # Check if the hash is valid
    if hash < target:
        #('Success!! Valid hash found.')
        payload = '{"params": ["' + address + '", "' + job_id + '", "' + extranonce2 + \
                   '", "' + ntime + '", "' + nonce + '"], "id": 1, "method": "mining.submit"}\n'
        sock.sendall(payload)
        #(sock.recv(1024))
        break  # Stop after successfully submitting the valid result
    else:
        #('Failed, hash is greater than target.')
        time.sleep(0.1)  # Optional: Slow down the loop a little to avoid overloading the server.

sock.close()
