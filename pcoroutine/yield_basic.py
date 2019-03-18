def yield_only():
    yield 1
    yield 2
    yield 3

def yield_and_send():
    ret = yield 1
    yield ret
