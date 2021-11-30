import requests

def reqType(testcase):
    if testcase.type == 'get':
        r = requests.request((testcase.type), url=(testcase.url), headers=(testcase.headers))
    else:
        if 'json' in testcase.headers['content-type']:
            r = requests.request((testcase.type), url=(testcase.url), json=(testcase.payload), headers=(testcase.headers))
        else:
            r = requests.request((testcase.type), url=(testcase.url), data=(testcase.payload), headers=(testcase.headers))
    return r