from pymongo import MongoClient


#建立MongoDB数据库连接
client = MongoClient('localhost', 27017)

#连接所需数据库,test为数据库名
db=client.test

#连接集合，即数据库表，test为表名
collection=db.test

#对数据库表常用操作(代码解释均已注释形式标记):
#向集合中插入一条数据
collection.insert({'name':'jim','age':23,'addr':'SCU'})
#向集合中插入多条数据
collection.insert_many([{'name':'lele','age':20,'addr':'Chengdu'},
                        {'name':'hans','age': 19, 'addr': 'Shenzhen'}])
#向集合中查询一条数据
res = db.test.find_one({"age": 19})
#向集合中查询全部数据（注意返回是游标，可用list或者for进行遍历）,可以使用$type为操作符，可以设置类型
# $gt = greater than  ls = less than  ne = negative  in / nin array(array 是你定义的list)
# $mod eg: db.test.find({"age":{"$mod":[10,1]}}) = 取模10后是否等于1
# $all 例如result=[1,2,3] require=[2,3] result满足 而[2,3,4]的话result不满足
# $size 匹配数组内元素数量
# $exist 判断数组内某元素是否存在
res = db.test.find({"age": {"$gt": 18}})
res = db.test.find({"name" : {"$type" : "string"}})
for r in res:
    print(r)
#向集合中更新第一条满足条件的数据
# 参数说明：
# criteria：查询条件
# objNew：update对象和一些更新操作符
# upsert：如果不存在update的记录，是否插入objNew这个新的文档，True为插入，默认为False，不插入。
# multi：默认是false，只更新找到的第一条记录。如果为true，把按条件查询出来的记录全部更新。
db.test.update_one({"age": 19},{"$set": {"age": 100}})
#向集合中更新，如果不存在则插入且只更新第一条
db.test.update({"count":{"$gt":50}},{"$set":{"name":"c5"}},True,False)
# {$inc:{field:value}}的作用是对一个数字字段的某个field增加value
db.test.update({"name":"Jim"},{"$inc":{"age":5}})
#向集合中更新所有满足条件的数据
db.test.update_many({"age": 10},{"$set": {"age": 100}})
#向集合中删除第一条满足条件的数据
db.test.delete_one({"age": 10})
#向集合中删除所有满足条件的数据
db.test.delete_many({"age": 18})

#查找集合中所有数据
for item in collection.find():
    print (item)

#查找集合中单条数据
print (collection.find_one())

# #删除集合collection中的所有数据
collection.remove()
#
# #删除集合collection
collection.drop()
