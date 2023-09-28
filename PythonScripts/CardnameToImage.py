WHITELIST_CHARS = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')

def CardnameToImage(name:str) -> str:
    return ''.join(filter(WHITELIST_CHARS.__contains__, name)) + ".png"

def CardnameToPath(name:str, cubename:str) -> str:
    return f"ImageFiles/{cubename}/{CardnameToImage(name)}"

def CardnameToPathInternal(name:str, cubename:str) -> str:
    return f"../{CardnameToPath(name, cubename)}"

def CardnameToLink(name:str, cubename:str) -> str:
    return f"{CardnameToPath(name, cubename)}"
#https://github.com/cirion02/CirionCubeSite/