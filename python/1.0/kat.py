import os
def authors(names):
    return names
def licence(licence_name):
        return licence_name
def link(link):
    return link
def web(web):
    return web
def licenceFile(licence_file, open):
    if open == "read":
     if os.path.exists(licence_file):
      with open(licence_file, "r") as licence:
        licencer =  licence.read()
        return licencer
     else:
         return f"LICENCE {licence_file} not found"
    elif open == None or 0:
        return licence_file
