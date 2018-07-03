import pymongo
#连接mongodb
#连接方式一
client = pymongo.MongoClient('127.0.0.1',27017)
#连接方式二
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# #获取数据库
# jobs_db = client.jobs
# #获取数据库下面的集合
# jobdesc = jobs_db.jobdesc
# #查询所有的数据文档
# results = jobdesc.find()

# for dict in results:
#     print(dict)
# #results是一个 <pymongo.cursor.Cursor object at 0x7f59b84fc6a0> 类型
# print(results)


# result = jobdesc.find_one()
# print(result)





#如果数据库存在就获取   不存在就创建
db = client.meinv
##如果集合存在就获取   不存在就创建
model = db.model
decument1 = {
    'name':'tianjing',
    'age':'20',
    'class':'201',
    'higth':165,
}
decument2 = {
    'name':'tianjing2',
    'age':'22',
    'class':'202',
    'higth':160,
}
decument3 = {
    'name':'tianjing3',
    'age':'20',
    'class':'201',
    'higth':195,
}

#数据插入
# result = model.insert([decument1,decument2,decument3])
#返回的结果是一个列表,内容是每一个文档的id
# [ObjectId('5b29b7c081512d15ac70bdbf'), ObjectId('5b29b7c081512d15ac70bdc0'), ObjectId('5b29b7c081512d15ac70bdc1')]
# print(result)

#获取集合中的数据
# result1 = model.find()
# for dict in result1:
    # print(dict)

#获取一条数据
# result2 = model.find_one()  

# #条件查询
# result3 = model.find({'name':'tianjing2'})  
# for dict in result3:
#     print(dict)
# print(result3)
#获取跳过第一条  返回后两条的数据
result4 = model.find().skip(1).limit(1)
for dict in result4:
    print(dict)
# print(result4)