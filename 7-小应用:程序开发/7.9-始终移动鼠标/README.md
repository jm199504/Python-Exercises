## 7.9 始终移动鼠标

### 问题描述

电脑需要始终开放端口提供服务，但是鼠标键盘未动，电脑会自动熄屏（无法设置永不熄屏功能），因此设计了始终移动鼠标的脚本。


### 示例代码
```python
import pyautogui
import time

count = 1
while True:
    if count % 2:
        pyautogui.moveTo(100, 100)
    else:
        pyautogui.moveTo(200, 200)
    time.sleep(60)
    count += 1

```
