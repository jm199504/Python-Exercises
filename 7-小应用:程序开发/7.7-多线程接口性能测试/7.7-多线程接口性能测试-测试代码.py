import threading
import requests
import time


class PerformanceTester:
    def __init__(self, url, num_threads, num_requests):
        self.url = url
        self.num_threads = num_threads
        self.num_requests = num_requests
        self.success_count = 0
        self.failure_count = 0
        self.total_response_time = 0

    def send_request(self):
        for _ in range(self.num_requests):
            start_time = time.time()
            try:
                # 发送网络请求
                response = requests.get(self.url)
                if response.status_code == 200:
                    self.success_count += 1
                else:
                    self.failure_count += 1
            except requests.exceptions.RequestException as e:
                self.failure_count += 1
            finally:
                end_time = time.time()
                self.total_response_time += end_time - start_time

    def run_test(self):
        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.send_request)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"Total requests: {self.num_threads * self.num_requests}")
        print(f"Successful requests: {self.success_count}")
        print(f"Failed requests: {self.failure_count}")
        print(f"Average response time: {self.total_response_time / (self.num_threads * self.num_requests)} seconds")


if __name__ == '__main__':
    url = "http://127.0.0.1:5000/hello"  # 本地API的URL
    num_threads = 2  # 线程数
    num_requests = 10  # 每个线程发送的请求数

    tester = PerformanceTester(url, num_threads, num_requests)

    # 给服务一点启动的时间
    time.sleep(2)

    # 然后执行性能测试
    tester.run_test()
