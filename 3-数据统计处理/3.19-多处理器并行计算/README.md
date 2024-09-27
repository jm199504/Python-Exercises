## 3.19-多处理器并行计算

### 问题描述
面对计算量大的时候，尝试考虑利用多处理器的优势，实现并行计算。


### 示例代码

使用`joblib`第三方库实现

```python
import time
from joblib import Parallel, delayed


def square(num):
    time.sleep(1)  # 模拟耗时的计算操作
    return num ** 2


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    start_time = time.time()
    # 并行计算每个数字的平方
    # n_jobs=-1 表示使用所有可用的处理器内核
    results = Parallel(n_jobs=-1)(delayed(square)(num) for num in numbers)
    end_time = time.time()

    # 打印计算结果
    print(results)
    print("并行处理时间：", end_time - start_time)

```



