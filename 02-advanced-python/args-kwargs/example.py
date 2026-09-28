def call_api(url, *args, **kwargs):
    print(url, args, kwargs)

call_api("/tickets", 1, 2, method="GET", timeout=5)
params = {"method": "POST", "timeout": 3}
call_api("/users", **params)
