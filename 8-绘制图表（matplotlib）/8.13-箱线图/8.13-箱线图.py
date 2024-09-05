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

# 设置 Seaborn 的默认配色方案
sns.set()

# 使用 boxplot 绘制箱线图
# x = "labels" 用于指定 x 轴的分类变量
# y = "sepal length (cm)" 用于指定 y 轴的数值变量
# 箱线图展示了不同类别下“sepal length (cm)”的分布情况
sns.boxplot(x=irisdata["labels"], y=irisdata["sepal length (cm)"])

# 显示图
plt.show()