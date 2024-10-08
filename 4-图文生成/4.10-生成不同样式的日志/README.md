## 4.10-生成不同样式的日志

### 问题描述
针对debug/info/warning/error等不同级别的日志，采用不同的样式显示。

### 示例代码
```python
from loguru import logger

# 配置日志文件路径
logger.add("app.log", rotation="500 MB")  # 日志文件达到500兆字节时进行轮转

# 记录不同级别的日志
logger.debug("This is a debug message")
logger.info("This is an informational message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

# 记录异常
try:
    result = 10 / 0
except Exception as e:
    logger.exception("An exception occurred: {}", e)

```

