########################################################################################################################
#                                                   Lainupcomputer                                                     #
#                                                   ez_utils v1.0                                                      #
########################################################################################################################

import base64
import bcrypt
import hashlib
version = "v1.0"


def gen_password_hash(passwd: str):
    passwd = passwd.encode("utf-8")
    passwd = base64.b64encode(hashlib.sha256(passwd).digest())
    hashed = bcrypt.hashpw(passwd, bcrypt.gensalt(12))
    return hashed.decode()


def check_password(passwd: str, hashed: str):
    passwd = passwd.encode('utf-8')
    passwd = base64.b64encode(hashlib.sha256(passwd).digest())
    hashed = hashed.encode('utf-8')
    if bcrypt.checkpw(passwd, hashed):
        return True
    else:
        return False


def send_debug(code="", msg="", enable=True):
    if enable:
        print(f"!{code} : {msg}")

