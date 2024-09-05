# 8.12-图矩阵

### 问题描述

（1）生成数据集

（2）绘制图矩阵

### 示例输出

<img src="?raw=true" style="zoom:80%;" />

### 示例代码

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

# 加载 Iris 数据集
irisdata = load_iris()

# 将目标标签转换为列表
labels = list(irisdata.target)

# 将数据和标签转换为 pandas DataFrame
irisdata = pd.DataFrame(data=irisdata.data, columns=irisdata.feature_names)
irisdata['labels'] = labels  # 将标签添加到 DataFrame 中

# 查看 DataFrame 的列
print(irisdata.columns)

# 设置 Seaborn 的默认配色方案
sns.set()

# 使用 pairplot 绘制数据对的图矩阵
# `hue="labels"` 参数用于根据标签对数据进行颜色编码
sns.pairplot(irisdata, hue="labels")

# 显示图
plt.show()
```