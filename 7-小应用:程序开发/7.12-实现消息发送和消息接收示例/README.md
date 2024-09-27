## 7.12-实现消息发送和消息接收示例

### 问题描述

完成`sender.py`和`receiver.py`代码，前者用于发送消息，后者运行后持续接收，直至遇到键入中断。

### `receiver.py`示例

```
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'Hello Junming!'
 [x] Received b'Hello Junming!'  # 每运行一次sender.py即多一行消息
```

### 示例代码（sender.py）

```python
import socket
import time

def send_message(message):
    # 创建一个UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置目标地址
    server_address = ('localhost', 12345)
    
    try:
        # 发送消息
        print(f"Sending: {message}")
        sock.sendto(message.encode(), server_address)
    finally:
        sock.close()

if __name__ == "__main__":
    while True:
        message = input("Enter a message to send (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        send_message(message)
        time.sleep(1)  # 每次发送间隔1秒
```

### 示例代码（receiver.py）

```python
import socket

def start_receiver():
    # 创建一个UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 绑定到本地地址和端口
    sock.bind(('localhost', 12345))
    
    print("[*] Waiting for messages. To exit press CTRL+C")
    
    while True:
        try:
            # 接收消息
            data, addr = sock.recvfrom(1024)  # 最多接收1024字节
            print(f"[x] Received {data} from {addr}")
        except KeyboardInterrupt:
            print("\n[*] Exiting receiver.")
            break
    
    sock.close()

if __name__ == "__main__":
    start_receiver()
```

