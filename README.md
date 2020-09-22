# Python练习册（每天一个小程序）

https://img.shields.io/badge/{author}-{jm199504}-{blue}.svg

参考题目来源： https://github.com/Yixiaohan/show-me-the-code 

说明：本篇代码参考对小部分题目解答有所改动，仅供参考答题思路，所有代码均已运行成功，细节交流或指正错误可添加个人微信(jm199504)！



### 题目：

**第 0000 题：** 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 

<img src="/images/readme1.jpg" width="50%">

**第 0001 题：** 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

<img src="/images/readme2.jpg" width="30%">

**第 0002 题:** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。

**第 0003 题：** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。

**第 0004 题：** 任一个英文的纯文本文件，统计其中的单词出现的个数。

**第 0005 题：** 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

**第 0006 题：** 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

**第 0007 题：** 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

**第 0008 题：** 一个HTML文件，找出里面的**正文**。

**第 0009 题：** 一个HTML文件，找出里面的**链接**。

**第 0010 题：** 使用 Python 生成类似于下图中的**字母验证码图片**

**第 0011 题：** 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

```
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
```

**第 0012 题：** 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

**第 0013 题：** 用 Python 写一个爬图片的程序

**第 0014 题：** 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

```
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
```

请将上述内容写到 student.xls 文件中

**第 0015 题：** 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

```
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
```

请将上述内容写到 city.xls 文件中。

**第 0016 题：** 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

```
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
```

请将上述内容写到 numbers.xls 文件中。

**第 0017 题：** 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

```
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
```

**第 0018 题：** 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

```
    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <cities>
    <!-- 
    	城市信息
    -->
    {
    	"1" : "上海",
    	"2" : "北京",
    	"3" : "成都"
    }
    </cities>
    </root>
```

**第 0019 题：** 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

```
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 
	数字信息
-->

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

</numbers>
</root>
```

**第 0020 题（省略）：** [登陆中国联通网上营业厅](http://iservice.10010.com/index_.html) 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。

第0020题参考代码省略原因个人为移动用户且很难找到网络公开通话记录单。

**第 0021 题：** 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

 HMAC是密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code） 

**第 0022 题：** iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。

**第 0023 题：** 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

参考代码：/guestsbook

<img src="/images/readme4.png" width="30%">

**第 0024 题：** 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

参考代码：/todolist

<img src="/images/readme3.jpg" width="30%">

**第 0025 题：** 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。

```
例如，对着笔记本电脑吼一声“百度”，浏览器自动打开百度首页。

关键字：Speech to Tex
```

主要流程：注册相关语音识别SDK，将语音转换为文字命令， 使用模拟浏览器操作工具例如webbrowser、 selenium等执行即可实现，其主要学习点在于使用模拟浏览器操作部分，因此可以参考以下代码/工具。

第0025题参考工具：使用robotframework自动化测试软件说明

个人公众号链接：https://mp.weixin.qq.com/s/xsOSGr0sWOeRD3Eb9TsCsA

第0025题参考代码：使用selenium分析网易云音乐评论

个人Github Repositories链接：https://github.com/jm199504/Selenium-WordCloud 
