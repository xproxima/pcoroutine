from pcoroutine import yield_basic


def test_yield_only():
    yield_only = yield_basic.yield_only()
    # py3
    # assert 1 == yield_only.__next__()
    # py2
    # assert 1 == yield_only.next()
    assert 1 == next(yield_only)
    assert 2 == next(yield_only)
    assert 3 == next(yield_only)


def test_yield_and_send():
    yield_and_send = yield_basic.yield_and_send()
    assert 1 == next(yield_and_send)
    assert 3 == yield_and_send.send(3)
