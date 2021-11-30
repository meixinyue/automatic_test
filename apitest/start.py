from openexcel import Read_Ex
from reqtype import reqType
# time在这里的作用主要是等待的操作
import time
from datetime import datetime
from report import Report
from testcase import TestCase
from inputs_error import InputsError

def createxml():
    # 获得report实例
    report = Report(datetime.now())
    #从excel文件读取测试用例，组装成列表
    httpurl_data = Read_Ex().read_excel()

    # 开始执行用例
    for data in httpurl_data:
        try:
            testcase = TestCase(data)
        except InputsError as ex:
            print(ex)
            report.case(data.get('title','没有标题'), datetime.now())
            report.error_data(str(ex))
            report.settime()
            continue

        # 判断需要跳过的用例
        if testcase.skip.lower() == "true":
            # 写入跳过用例标题名
            report.case(testcase.title, datetime.now())
            # 跳过用例的信息
            report.skip_case('This testcase is skipped')
            report.settime()
            # continue 跳出本次循环不会结束循环
            continue

        # 这条用例开始执行的时间
        case_time = datetime.now()
        # 使用sleep进行等待
        time.sleep(int(testcase.time))

        r = reqType(testcase)

        # 用例通过
        reason = ''       #失败用例失败原因
        result = True       #测试结果
        if r.status_code == 200:

            for asserts in testcase.asserts:
                # 每个字段和去接口的返回值去对比
                if asserts not in str(r.text):
                    result = False
                    reason = asserts + '断言失败'
        else:
            result = False
            reason = '状态码为 ' + str(r.status_code)

        # 用例通过
        if result:
            # 写入xml测试报告
            report.case(testcase.title, case_time)
            report.settime()
        # 用例不通过
        else:
            report.case(testcase.title, case_time)
            report.failure('标题：' + testcase.title + '  请求类型：' + testcase.type +'   失败原因：' + reason)
            report.settime()

    # 生成xml数据源 提供给allure
    # 生成测试套件 参数为用例的总数int类型，测试项目名称string类型
    report.set_suite(len(httpurl_data),'接口测试')
    report.settime()
    # 生成xml
    report.write_toxml()

if __name__ == '__main__':
    createxml()