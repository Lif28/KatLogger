def authors(names):
    return names
def licence(licence_name, licence_file):
    with open(licence_file, "r") as licence:
        licencer =  licence.read()
        return licence_name, licencer
def link(link):
    return link
def web(web):
    return web
