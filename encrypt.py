import hashlib

def sha1(value):
    h = hashlib.new("sha1", value.encode())
    return h.hexdigest()