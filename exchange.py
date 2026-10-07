def calculator(a,b,c):
    import numpy as np
    import http.client

    conn = http.client.HTTPSConnection("api.fxratesapi.com")
    conn.request("GET", "/latest?currencies=" + a + "&base=" + b + "&amount=" + c + "&api_key=fxr_live_5351ce42c4490c4430ad737c09b91f460db3")

    res = conn.getresponse()
    data = res.read()

    exli = data.decode("utf-8")

    ans = exli[exli.find(a)+5:-3]

    print(c + " in " + b + " is " + ans + " in " + a + ".")
    return (c + " in " + b + " is " + ans + " in " + a + ".")

