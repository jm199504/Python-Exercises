## Python 练习册（基础操作/数据库/数据统计处理/图文生成/数据转换/算法题/笔试题/小应用/程序开发）

![author](https://img.shields.io/static/v1?label=Author&message=junmingguo&color=green)
![language](https://img.shields.io/static/v1?label=Language&message=python3&color=orange) ![topics](https://img.shields.io/static/v1?label=Topics&message=python&color=blue)

【知乎】：[Python练习册专栏链接](https://www.zhihu.com/column/c_1706758542932103168)

## 题目分类

### 一、算法题/笔试题

#### 1.1 密码游戏

- 牛牛和牛妹一起玩密码游戏，牛牛作为发送方会发送一个4位数的整数给牛妹，牛妹接收后将对密码进行破解。

#### 1.2 蜗牛多久能爬上去

- 有一棵光滑的葡萄树高 18 分米，一只蜗牛从底部向上攀，每分钟爬 3 分米，但每爬一分钟后都要休息一分钟，休息期间又要滑下 1 分米。请问最快在第几分钟，蜗牛可以爬到树顶端。

#### 1.3 画满天五角星

- 老师布置了一个作业要小盆友画五角星，并且需要画很多个，但是小明想偷懒，所以准备用Python来画五角星。

#### 1.4 排列组合

- 提供三个字符，比如：a、b、c，需要输出所有组合情况，组合里可重复字符。

#### 1.5 菱形图案

- 打印用“*”组成的菱形图案。

#### 1.6 递归计算兔子的数量

- 兔子的数量以这样的方式增长：每个月的兔子数量等于它前一个月的兔子数量加它前两个月的兔子数量，即`f(n)=f(n-1)+f(n-2)`。假设第1个月的兔子有2只，第2个月的兔子有3只，你能使用递归的方法求得第n个月的兔子有多少只吗？

#### 1.7 球的表面积

- 计算球的表面积

#### 1.8 最长连续序列

- 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

#### 1.9 轮转数组

- 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

#### 1.10 最大数

- 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

#### 1.11 反转链表

- 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


#### 1.12 快速排序

- 给你一个整数数组 nums ，使用快速排序对 nums 进行排序。

#### 1.13 冒泡排序

- 给你一个整数数组 nums ，使用冒泡排序对 nums 进行排序。

#### 1.14 最长回文子串

- 给定一个字符串 s，输出 s 中最长的回文子串，其中回文子串指该子串倒序与正序相同。

#### 1.15 整数反转

- 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转，有效数值范围为 [(−2)^31, 2^31 − 1]，若超出有效数值范围则输出 0。

#### 1.16 无重复字符的最长子串

- 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

#### 1.17 最长公共前缀

- 编写一个函数来查找字符串数组中的最长公共前缀。 如果不存在公共前缀，返回空字符串 ""。

#### 1.18 三数之和

- 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
  同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

#### 1.19 回文数

- 判断一个数字是否为回文数，如果从左边和右边读的结果是一样的则是回文数，若为回文数返回True，反之返回False。

#### 1.20 字符串相乘

- 传入一个字符串和一个数值，输出的结果是将字符串重复数值的次数。

#### 1.21 全排列

- 给定一个不含重复数字的数组 nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。

#### 1.22 两数之和

- 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

#### 1.23 最大子数组和

- 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和，子数组是数组中的一个连续部分。

#### 1.24 01背包

- 输入两个整数*n,m ,n表示你拥有的积分，m表示有多少礼品，接下来有m行，每行a和b，a表示物品所需要消耗的积分，b表示这个物品大家的喜爱值，a和b取值范围是[1,100]，装入最多的喜爱值。

#### 1.25 两数之和

- 给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。


#### 1.26 两两相等数有一个不等数

- 给定一个整数数组里面有很多整数，基本都是两两相等，但是存在一个不等数，请输出这个不等数。

#### 1.27 蛇形座位表

- 现在有一个会场需要您进行座位排序，你希望ID临近的参会人员挨着坐，所以你想到了蛇形座位表，提供你一份ID列表，比如：[1,2,3,4,5,6,7...,87]，每一排是10位，请生成一份二维数组，并且存储到excel表。

#### 1.28 统计函数运行时长

- 一个流程涉及调用多个函数，但最近发现流程整体运行时间慢，现需要对每一个函数统计运行时长。

---

### 二、数据库

#### 2.1 插入MySQL数据库

- 将生成促随机码题目生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

#### 2.2 插入Redis数据库

- 将生成随机码题目生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

#### 2.3 MongoDB数据库基本交互

- 数据库链接、向集合插入数据、查询数据、删除指定数据、查询数据

---

### 三、数据统计处理

#### 3.1 统计单词数量

- 一个英文的纯文本文件，统计其中的单词出现的个数

#### 3.2 统计最重要的词

- 一个日记目录（ txt格式），为避免分词的问题，假设内容都是英文，统计出每篇日记最重要的词。

#### 3.3 统计代码行数

- 一个代码目录，统计一下写过多少行代码。包括空行和注释，分别列出来。

#### 3.4 统计HTML各类内容

- 一个HTML文件，找出里面的标题、内容、链接、正文内容

#### 3.5 敏感词识别

- 一个敏感词文本文件，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

#### 3.6 敏感词替换*

- 一个敏感词文本文件，当用户输入敏感词语，用星号`*`替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

#### 3.7 统计数据空值

- 如果你想知道某csv数据文件每一列的信息是否都有完整数据。

#### 3.8 统计谁在用Python语言

- csv文件，包含用户ID、等级、所使用的编程语言的字段，现输出有谁在用Python这一门语言，并且希望按照等级降序输出显示，若等级相同时，请按照用户ID升序，注意大小写忽略。

#### 3.9 统计哪个语言最多人用

- csv文件包含用户ID、等级、所使用的编程语言的字段，请按照编程语言使用人数降序，并输出各个语言的使用人数。

#### 3.10 仅查看前后前几行

- csv文件包含用户ID、等级、所使用的编程语言的字段，现需要仅读取前几行数据，或者后几行数据。

#### 3.11 统计Python高阶玩家

- csv文件包含用户ID、等级、所使用的编程语言的字段，现需要输出编程语言（language）使用Python并且等级（level）≥4的用户信息。

#### 3.12 统计数字3

- 编写一个count(3)函数统计1-100以内有几个数字3

#### 3.13 统计指定日期数量

- 一份数据包含time字段，包含了年/月/日 小时:分钟，客户更关心指定日期的数据量，现需要进行统计。

#### 3.14 统计昨今返场用户

- 有一个打卡活动需要统计：当天打卡用户是否在昨日也打卡过，现需要输出每一天打卡用户中在前一日也打过卡的用户名称。

#### 3.15 矩阵（二维数组）相加

- 计算两个矩阵（二维数组）相加

#### 3.16 双值互换

- 提供多种方法实现a和b变量值互换

#### 3.17 字典合并

- 合并字典

#### 3.18 读取txt文件统计字符个数

- 为了读取txt文件并统计字符个数，同时设计测试用例，你可以编写一个Python脚本，其中包含统计字符个数的函数以及相应的测试函数。这里使用unittest模块来进行测试。

#### 3.19 多处理器并行计算

- 面对计算量大的时候，尝试考虑利用多处理器的优势，实现并行计算。

---

### 四、图文生成

#### 4.1 生成微信头像消息

- 请将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

#### 4.2 生成随机码

- 作为 Store App 独立开发者，你需要为你的应用生成随机码，使用 Python 如何生成 200 个随机码？

#### 4.3 生成验证码

- 生成类似于文末的字母验证码图片。

#### 4.4 用户密码加密存储

- 某个网站或者 APP后台管理需要使用HMAC对密码加密。

#### 4.5 缩小图片至指定大小

- 一个照片目录，统一修改尺寸修改不大于 iPhone5 分辨率的大小（iPhone5 分辨率：1136×640像素）

#### 4.6 制作词云

- 一个文本文件的重要词汇抽离生成词云。

#### 4.7 生成二维码

- 将文本或者链接以二维码的形式保存，同时将制定图片插入二维码或者设置为背景。

#### 4.8 凯撒密码对输入字符串进行加密

- 接受一个字符串和一个移位值作为参数，然后返回加密后的字符串。加密过程是通过将字符串中的每个字母字符按照移位值进行循环移位来实现的，非字母字符保持不变。

#### 4.9 文本生成手写图片

- 将文本转为手写体的图片。

#### 4.10 生成不同样式的日志

- 针对debug/info/warning/error等不同级别的日志，采用不同的样式显示。

#### 4.11 生成箱体文本

- 针对英文文本用箱体包裹的样式，用于标识关键信息。

#### 4.12-生成随机数by-random

- 使用random库生成各类随机数

---

### 五、数据转换

#### 5.1 字典文本转表格

- 字典txt文件转为excel文件。

#### 5.2 表格转XML

- excel转为txt文件。

#### 5.3 JSON转表格

- JSON数据转为Excel格式。

#### 5.4 JSON转字典 & 字典转JSON

- 将dict对象和string对象互转；将dict对象存储到JSON文件，从JSON文件读取dict数据

#### 5.5 unix时间戳转字符串

- 目前有很多在线Unix时间戳(timestamp)转换工具，如何用Python实现这一功能。

#### 5.6 列表文本转表格

- 列表txt文件转为excel文件。

#### 5.7 优化日期格式

- 一个CSV文件，其中的日期格式统一为mm/dd/yyyy，期望将日期格式统一转为YYYY年mm月dd日。

#### 5.8 字典转YAML

- 有一份python的字典（dict）对象，需要转为YAML格式。

#### 5.9 YAML转字典

- 有一份YAML格式，需要转为python的字典（dict）对象。

#### 5.10 字典转PDF

- 有一份python的字典（dict）对象，需要转为PDF格式。

#### 5.11 URL编码转为字符串

- 部分网页接口返回的数据是URL编码后的字符，无法直接阅读，需要转为可阅读的字符串。

#### 5.12 结合变量值将模板文件中的动态内容生成HTML页面

- 结合变量值将模板文件中的动态内容生成HTML页面，实现生成新的HTML页面。

---

### 六、文件命令操作

#### 6.1 批量文件重命名

- 笔记软件导出笔记到markdown格式，md文件名不符合预期，存在一串不明字符，现需要批量修改。

#### 6.3 根据文件标题和内容生成目录

- 将一个文件夹内的md5文件中的标题和指定内容转为目录。

#### 6.4 执行命令行命令

- 在py文件里面执行`touch **.txt`的命令，创建10个txt文件，分别为`1-10.txt`。

### 七、小应用/程序开发

#### 7.1 留言簿应用

- 基于 Python 的 Web 框架的Web 版本留言簿应用。

#### 7.2 FTP文件分享

- 小A和小B在共同完成课件，希望直接通过拖拽的方式放入指定文件夹进行素材文件共享。

#### 7.3 API方式调用百度翻译

- 用API方式调用百度翻译接口，实现在终端输入中文，返回英文结果。

#### 7.4 待办事项应用开发

- 基于 Python 的 Web 框架的 Web 版本 TodoList 应用。

#### 7.5 积分榜

- 玩游戏：四位玩家需要记录每一轮得分，并且实时统计总分。

#### 7.6 基于flask的用户登录和注册系统

- 基于flask框架实现用户登录和注册系统

#### 7.7 多线程接口性能测试

- 设计一个多线程的性能测试框架，用于测试一个网络服务的并发能力和响应时间，需要本地搭建一个后端服务并暴露接口用于测试。

#### 7.8 使用pytest测试

- 测试一个简单的用户管理系统，包括用户创建、用户验证和用户信息更新的功能。

#### 7.9 始终移动鼠标

- 电脑需要始终开放端口提供服务，但是鼠标键盘未动，电脑会自动熄屏（无法设置永不熄屏功能），因此设计了始终移动鼠标的脚本。

#### 7.10 实现一个随机丢球程序界面

- 有一个单独窗体程序，实现点击鼠标即释放一个球，并随机碰撞窗体的边框实现弹起行为。

#### 7.11 实现一个简单的问答系统

- 提供以下的问题与答案库，实现文本匹配回答问题

| question               | answer                                               |
| ---------------------- | ---------------------------------------------------- |
| 中国总面积             | 中国的总面积约为960万平方公里（约为370万平方英里）。 |
| 陆地上最大的动物是什么 | 大象                                                 |
| 中国总人口             | 截至2022年，中国的人口约为14亿。                     |

#### 7.12 实现消息发送和消息接收示例

- 完成`sender.py`和`receiver.py`代码，前者用于发送消息，后者运行后持续接收，直至遇到键入中断。

---

### 八、绘制图表（matplotlib）

#### 8.1 折线图（plot）
折线图通过连接数据点来展示数据的趋势和变化，非常适合展示时间序列数据。

#### 8.2 折线图子图（plot-sub）
折线图子图允许在一个图形窗口中展示多个折线图，方便比较不同数据系列的趋势。

#### 8.3 柱状图（bar）
柱状图通过柱子的高度或长度来展示不同类别的数量或频率，适合比较各类别之间的大小。

#### 8.4 饼图（pie）
饼图用于显示各部分在整体中所占的比例，以圆形分割的方式展示每部分的相对大小。

#### 8.5 散点图（scatter）
散点图使用点的分布来展示两个变量之间的关系或相关性，帮助识别数据中的模式或趋势。

#### 8.6 等高线图（contourf）
等高线图展示了不同变量的值在二维平面上的变化，使用等高线表示相同值的区域，适合显示地形或函数的轮廓。

#### 8.7 堆叠图（stack）
堆叠图通过叠加不同系列的图形展示各部分对整体的贡献，适合展示累计数据的变化。

#### 8.8 直方图（hist）
直方图将数据分成若干区间，通过条形图展示每个区间内的数据频数，适合展示数据的分布情况。

#### 8.9 热量图（heatmap）
热量图通过颜色强度展示数据矩阵中的值，常用于显示数据密度或相关性。

#### 8.10 热图（heatmap）
热图类似于热量图，但通常用于显示更复杂的数据矩阵，能通过颜色编码的方式显示数据的强度和模式。

#### 8.11 联合图（joint）
联合图展示了两个或更多变量之间的联合分布，通常结合散点图和直方图来显示数据的关系和分布情况。

#### 8.12 图矩阵（pair）
图矩阵通过绘制所有特征对的散点图来展示数据集的特征之间的关系，适合进行数据探索和模式识别。

#### 8.13 箱线图（box）
箱线图展示了数据的分布、中心值、以及异常值，通过箱子的形状和须的长度展示数据的统计特征。

#### 8.14 3D散点图（3D-scatter）

散点图可直观地展示三个连续变量之间的关系。

#### 8.15 小提琴图（violinplot）

小提琴图是一种可视化数据分布和密度的图表类型。它显示了数据的整体分布形状以及估计的核密度曲线。

#### 8.16 六边形箱图（hexbin）

六边形箱图是一种可视化二维数据分布的图表类型。它将数据按照坐标轴划分为多个小六边形区域，并根据每个区域内数据点的数量进行不同的着色，以展示数据分布情况。

#### 8.17 箭头图（arrow）

箭头图是用于绘制箭头的图表类型。它可以用于表示矢量或方向数据。

#### 8.18 极坐标图（polar）

极坐标图是一种用于显示圆形数据或周期性数据的图表类型。它使用极径和极角来表示数据点的位置。

#### 8.19 误差棒图（errorbar）

误差棒图（error bar plot）是一种用于可视化数据的中心趋势和误差范围的图表类型。它通常在数据点周围绘制直线或线段，表示数据的误差或不确定性。

---

### 九、绘制图表（pyecharts）

#### 9.1 柱状图（bar）
柱状图通过柱子的高度展示各类别的数量或值，适合用于比较不同类别之间的数据。

#### 9.2 柱状阵-XY轴互换（bar-YX）
柱状阵图通过交换X轴和Y轴来展示数据，适合需要对比类别数量的情况，并以不同的维度展示数据。

#### 9.3 饼图（pie）
饼图显示各部分在整体中所占的比例，帮助了解每部分相对整体的贡献情况。

#### 9.4 词云（wordcloud）

词云图是一种用于可视化文字数据的图表类型。它通过将不同词语的频率反映为词语的大小，以形成一个具有视觉吸引力的图形来展示文字数据的重要性或热门程度。

#### 9.5 树状图（treemap）

树状图是一种用于可视化层次结构数据的图表类型。它通过矩形的大小和颜色来展示数据的分布情况，其中每个矩形代表一个节点，节点的大小表示其在层次结构中的权重或大小，颜色可以用来表示其他维度的数据。

#### 9.6 树形图（tree）

树形图是一种用于展示树形结构数据的图表类型，它以一个根节点为起点，通过连接多个子节点来表示层次结构。每个节点可以包含子节点，形成一个树的结构。

#### 9.7 时间轴（timeline）

时间轴在水平轴上显示时间线，垂直轴上显示相关事件的名称和说明。时间线上通常标出了重要的日期和时间点。

#### 9.8 表格（table）

表格可以理解为Office的Excel表格搬到了pyecharts。

#### 9.9 雷达图（radar）

雷达图是一种以圆形坐标系（也称极坐标系）为基础的图表类型，它可以用于多个指标之间的比较。在雷达图中，每个指标会对应到一个半径，不同的数据系列会在同一个雷达图上绘制，通过各自的半径值和角度范围展示数据之间的对比情况。例如，你可以用雷达图来比较不同城市的空气质量指数（AQI），其中每个城市对应一个数据系列，各个指标对应不同的半径，比如 PM2.5、PM10、O3 等。

#### 9.10 极坐标图（polar）

极坐标图是一种常用的数据可视化图表，用于展示数据在圆形坐标系中的分布情况。它适用于显示具有方向和距离属性的数据，例如在不同方向上的各个指标的相对大小或周期性数据的变化情况。

#### 9.11 象形柱图（pictorialbar）

象形柱图通过简单的图像符号代替普通柱子来表示数字的相对大小。这些符号通常是可视化对象的图像或其他象征性的符号，它们的大小、颜色或数量都可以反映与数据点相关的其它信息。

#### 9.12 重叠图（overlap）

重叠图将多个不同类型的图表叠加在一个坐标系中，从而实现多图表的对比展示。

#### 9.13 液态图（liquid）

液态图是一种用于展示百分比或比例的特殊图表类型。它类似于进度条，但是可以显示更多的精确度，并且通常用于显示固定总量中的部分数量。

#### 9.14 图（graph）

图用于可视化节点和节点之间的关系。它通常用于表示网络、社交关系、组织架构和知识图谱等图形结构。

#### 9.15 地理图（geo）

地理图用于绘制地理图。Geo 可以绘制国内外各省市、各国家的地理信息，包括地图、热力图、散点图等。

#### 9.16 仪表盘（gauge）

仪表盘主要用于表示一个度量值的当前值与其标准值、最小值、最大值之间的关系。Gauge 图表通常具有表盘和指针两个核心元素。

#### 9.17 漏斗图（funnel）

漏斗图是一种用于显示阶梯式数据的图表类型。漏斗图主要用于展示有序的数据序列，在不同的阶段或步骤之间的数量逐渐减少的情况下，帮助观察者直观地理解数据的流动和转化过程。

#### 9.18 K线图（kline）

K线图是一种常用于展示金融市场数据的图表类型。它主要用于显示一段时间内的开盘价、最高价、最低价和收盘价等数据。K线图通常用于股票、期货、外汇等交易市场的技术分析，可以帮助分析师和交易者快速了解价格的变化趋势和波动情况。

#### 9.19 箱线图（boxplot）

箱线图是一种用于显示数值数据分布的图表类型。它以一组数据的统计特征为基础，包括中位数、上下四分位数、最小值和最大值，并通过绘制箱体和触须来展示这些统计特征。

#### 9.20 日历图（calendar）

日历图根据时间数据绘制每天的数据（如商品销售情况、网站流量等）在整个时间范围内的分布情况。

#### 9.21 热力图（heatmap）

热力图是一种用来展示数据密度和模式的图表类型。

#### 9.22 散点图（scatter）

散点图是一种用来展示两个变量之间关系的图表类型。

#### 9.23 折线图（line）

折线图用于展示随时间、连续性或有序数据发展的趋势。
