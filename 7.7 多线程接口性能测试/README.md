## 7.7 多线程接口性能测试

### 问题描述
设计一个多线程的性能测试框架，用于测试一个网络服务的并发能力和响应时间，需要本地搭建一个后端服务并暴露接口用于测试。

相关需求如下：
1、使用flask搭建/hello接口，接口可考虑返回"Hello World!"
2、尝试用多线程测试接口的响应时间，其中status code为200时表示请求成功
3、性能测试结果输出需要包含以下字段： 
- Total requests
- Successful requests
- Failed requests
- Average response time

