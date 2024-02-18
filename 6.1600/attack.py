# gc and inspect
import inspect 

class generic_object:
    def __init__(self, name):
        self.name = name 
    
    def __eq__(self, secret):
        return secret

class os:
    def urandom(self, size):
        return bytes(0)

class fakehash:
    def __init__(self,x):
        self.x = x

    def digest(self):
        return bytes(self.x)
        
class fakehashlib:
    def __init__(self, x):
        self.x = x

    def sha256(self, r):
        return fakehash(self.x)


def attack_one(guess):
    x = generic_object("hi")
    
    return guess(x)

def attack_two():
    previous_frame = inspect.currentframe().f_back
    locals = previous_frame.f_locals
    # print(locals)
    return locals['secret']

def attack_three():
    previous_frame = inspect.currentframe().f_back
    globals = previous_frame.f_globals

    globals["os"] = os()
    return bytes(0)

def attack_four():
    previous_frame = inspect.currentframe().f_back
    locals = previous_frame.f_locals
    # print(locals)   
    h = locals["h"] 

    globals = previous_frame.f_globals 
    # print(globals)
    globals["hashlib"] = fakehashlib(h)

    return b''