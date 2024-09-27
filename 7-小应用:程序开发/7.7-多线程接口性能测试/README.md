## 7.7-多线程接口性能测试

### 问题描述
设计一个多线程的性能测试框架，用于测试一个网络服务的并发能力和响应时间，需要本地搭建一个后端服务并暴露接口用于测试。

### 相关需求
1、使用flask搭建/hello接口，接口可考虑返回"Hello World!"
2、尝试用多线程测试接口的响应时间，其中status code为200时表示请求成功
3、性能测试结果输出需要包含以下字段： 
- Total requests
- Successful requests
- Failed requests
- Average response time

### 示例代码（Flask应用文件 app.py）

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 示例文件（多线程性能测试）

```python
# performance_test.py
import requests
import threading
import time

class PerformanceTester:
    def __init__(self, url, total_requests):
        self.url = url
        self.total_requests = total_requests
        self.successful_requests = 0
        self.failed_requests = 0
        self.response_times = []

    def send_request(self):
        start_time = time.time()
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.successful_requests += 1
            else:
                self.failed_requests += 1
        except Exception as e:
            self.failed_requests += 1
        end_time = time.time()
        self.response_times.append(end_time - start_time)

    def run_test(self):
        threads = []
        for _ in range(self.total_requests):
            thread = threading.Thread(target=self.send_request)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def report_results(self):
        total_requests = self.total_requests
        average_response_time = sum(self.response_times) / total_requests if total_requests > 0 else 0
        print(f"Total requests: {total_requests}")
        print(f"Successful requests: {self.successful_requests}")
        print(f"Failed requests: {self.failed_requests}")
        print(f"Average response time: {average_response_time:.4f} seconds")

if __name__ == '__main__':
    tester = PerformanceTester(url='http://127.0.0.1:5000/hello', total_requests=100)
    tester.run_test()
    tester.report_results()
```

### 测试命令

```
python3 app.py

python3 performance_test.py
```

