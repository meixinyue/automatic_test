from xml.dom.minidom import Document
from pathlib import Path
import time
from datetime import datetime
from config import reportdir

class Report:

    def __init__(self, pstarttime):
        self.doc = Document()
        self.pstarttime = pstarttime
        self.testsuites = self.doc.createElement('testsuites')
        self.doc.appendChild(self.testsuites)
        self.nowtime = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        self.testsuite = self.doc.createElement('testsuite')

    def set_suite(self, num, name):
        self.testsuite.setAttribute('tests', str(num))
        self.testsuite.setAttribute('name', name)
        self.testsuite.setAttribute('timestamp', str(datetime.isoformat(self.pstarttime)))

    def case(self, title, time):
        self.testcase = self.doc.createElement('testcase')
        self.testcase.setAttribute('name', str(title))
        self.case_timer = time

    def skip_case(self, message):
        skip = self.doc.createElement('skipped')
        skip.setAttribute('message', message)
        self.testcase.appendChild(skip)

    def error_data(self, message):
        errordata = self.doc.createElement('skipped')
        errordata.setAttribute('message', message)
        errordata.setAttribute('type', 'errordata')
        self.testcase.appendChild(errordata)

    def settime(self):
        endtime = datetime.now()
        td = endtime - self.case_timer
        time = float(td.microseconds + (td.seconds + td.days * 24 * 3600) * 1000000) / 1000000
        self.testcase.setAttribute('time', str(time))
        self.testcase.setAttribute('priority', 'M')
        self.testsuite.appendChild(self.testcase)

    def failure(self, message):
        failure = self.doc.createElement('failure')
        failure.setAttribute('message', str(message))
        failure.setAttribute('type', 'Failure')
        self.testcase.appendChild(failure)

    def write_toxml(self):
        td = datetime.now() - self.pstarttime
        td_time = float(td.microseconds + (td.seconds + td.days * 24 * 3600) * 1000000) / 1000000
        self.testsuite.setAttribute('time', '%s' % td_time)
        self.testsuites.appendChild(self.testsuite)

        files = (reportdir, )
        for k in files:
            path = Path(k)
            if path.is_file():
                index = '(0)'
                for i in range(1, 10):
                    index = '(' + str(i) + ')'
                    path = Path(k + index)
                    if not path.is_file():
                        break

            if not path.is_dir():
                path.mkdir()

        file = path / ('API-Report@' + self.nowtime + '.xml')
        f = open(file, 'w', encoding='utf-8')
        self.doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()