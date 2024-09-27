## 2.3-MongoDB数据库基本交互

### 基础介绍

MongoDB是一个基于分布式文件存储的数据库，是由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案，MongoDB 是一个介于关系数据库和非关系数据库之间的产品。

特点：高性能、易部署、易使用，存储数据非常方便。

主要功能特性：

* 面向集合存储，易存储对象类型的数据。

* 模式自由。

* 支持动态查询。

* 支持完全索引，包含内部对象。

* 支持查询。

* 支持复制和故障恢复。

* 使用高效的二进制数据存储，包括大型对象（如视频等）。

* 自动处理碎片，以支持云计算层次的扩展性。

* 支持RUBY，PYTHON，JAVA，C++，PHP，C#等多种语言。

* 文件存储格式为BSON（一种JSON的扩展）。

* 可通过网络访问。

### 相关库/管理工具

核心第三方库pymongo

可视化软件mongoDB Compass管理工具

### 安装和配置MongoDB环境

MongoDB官网：https://www.mongodb.com/

①进入官网打开下载页面

②安装过程简单（安装中可以选择Custom来自定义安装路径）

安装成功后打开安装目录，介绍一下里面的文件：

mongo.exe——使用数据库（类似于：客户端）

mongod.exe——使用数据库和开启服务（类似于：服务端）

mongodump.exe——数据备份

mongoexport.exe——数据导出

mongoimport.exe——数据导入

mongorestor.exe——数据还原

③配置Mongodb，在C盘或者D盘创建两个文件夹分别是

C:\data\db——存放数据库文件

C:\data\log——存放数据库日志文件

④添加环境变量

(1)安装过python的小伙伴都知道如何添加了，我还是在重复一下流程：

计算机—右键—属性—高级系统设置—环境变量—系统变量—path—将MongoDB安装目录下的lib绝对路径加入path中

(2)检验环境变量是否配置成功，确定(1)后打开运行>path，看看环境变量是否加入成功

⑤启动MongoDB服务(我的data文件夹新建在C盘)

运行>mongod.exe --dbpath=C:\data\db

⑥注意⑤启动成功后不要关闭控制台，再新建一个控制台

运行>mongo

如果完成以上6步后恭喜你已经安装及环境配置成功！

接下来可以设置一下mongoDB随着系统启动自动开启：

⑦运行

```
\>mongod.exe --dbpath=C:\data\db --logpath=C:\data\log\MongoDB.log --install

\>net start mongodb

\>mongo
```

### 连接流程

①与MongoDB数据库连接

①与MongoDB数据库连接

②连接指定具体数据库

③连接指定数据库下指定的具体数据库表

### MongoDB常用命令及可视化

(1)介绍下MongoDB的常用命令：

启动运行>mongo

①查看所有的数据库：

`show dbs`

②从指定主机克隆数据库：

`db.cloneDatabase("192.168.1.100")`

③从指定的机器上复制指定数据库数据到某数据库：

\#将192.168.1.100的test的数据复制到new_test数据库中

`db.copyDatabase("test","new_test","192.168.1.100")`

④查看当前使用的数据库

`db.getName()`

⑤删除当前使用的数据库

`db.dropDatabase()`

⑥修复当前数据库

`db.repairDatabase()`

⑦获得当前数据库的所有聚集集合，即当前数据库的数据库表

`db.getCollectionNames()`

⑧查询记录/文档(举个带有条件的查询)

`db.test.find({"age":23})`

⑨查询前5条记录/文档

`db.test.find({'name':'jim'}).limit(5)`

### MongoDB Compass管理工具相关说明

①在MongoDB中数据库称为DBS，数据库表称为COLLECTIONS，记录称为DOCUMENT（可以LIST和TABLE形式查看）

②使用FIND查询，查询格式{字段名：查询条件}

③在Explain Plan中可以查看语句解释执行计划

④Indexs是索引，可以为集合创建索引及查看集合下的索引信息

⑤Aggregate是聚合管道，可以对数据进行分组过滤等操作，pipeline常用参数介绍：

- $project 可以自定义哪些字段显示与不显示

- $match 根据条件过滤数据

- $limit 限制聚合管道返回的文档数

- $skip 跳过指定数量的文档

- $group 将集合中的文档分组，统计结果

