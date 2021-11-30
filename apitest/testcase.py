import json
from inputs_error import InputsError

class TestCase:

    def __init__(self, data):
        self.title = data.get('title', '没有标题')
        self.skip = data.get('skip')
        self.url = data.get('url')
        self.headers = data.get('headers')
        self.payload = data.get('payload')
        self.type = data.get('type')
        self.time = data.get('time', 0)
        self.asserts = list(data.get('assert').split('/'))


        request_type = ['get', 'post', 'options', 'head', 'delete', 'put', 'connect']

        if self.url is None:
            raise InputsError('接口数据不对，缺少url')
        else:
            if self.type is not None:
                if self.type.lower() not in request_type:
                    raise InputsError('请求类型输入不正确,输入为：' + self.type)
            else:
                raise InputsError('接口数据不对，缺少请求类型')

        if self.time == '':
            self.time = 0
        else:
            try:
                int(self.time)
            except:
                raise InputsError('延迟时间不对')

        if self.headers != '':
            self.headers = json.loads(self.headers)
        else:
            self.headers = None

        if self.payload != '':
            self.payload = json.loads(self.payload)