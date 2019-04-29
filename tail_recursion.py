# =====================================================================
# tail_recursion.py
#
# ALL CREDIT GOES TO: Chris Penner
# SEE: https://chrispenner.ca/posts/python-tail-recursion
#
# I did not write this, I'm just using this to speed up the recursion
# =====================================================================

class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)

def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue

    return decorated