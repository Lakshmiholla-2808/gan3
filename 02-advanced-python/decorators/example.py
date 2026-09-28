import functools, time

def retry(times=3):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            for n in range(1, times + 1):
                try:
                    return fn(*a, **kw)
                except Exception as e:
                    print(f"attempt {n} failed: {e}")
            raise RuntimeError("all retries failed")
        return wrapper
    return deco

calls = {"n": 0}

@retry(times=3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("network")
    return "ok"

print(flaky())
