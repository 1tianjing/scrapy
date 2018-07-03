import pymongo
#连接mongodb
#连接方式一
client = pymongo.MongoClient('127.0.0.1',27017)
#连接方式二
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')




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
    'age':'21',
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



# #获取跳过第一条  返回后两条的数据
# result4 = model.find().skip(1).limit(1)
# for dict in result4:
#     print(dict)
# # print(result4)


#更新数据
# result = model.update({'name':'tianjing2'},{'$set':{'hight':200}})
# print(result)


#查看更新后的结果是否正确
# result = model.find_one({'name':'tianjing2'})
# print(result)



#根据年龄排序
# result = model.find().sort('age',1)  #升序
#result = model.find().sort('age',-1)  #降序
#for dict in result:
#    print(dict)

#save和update的区别:如果update 更新的内容在集合中不存在,就无法更新,如果save更新的内容在集合中不存在就会直接插入一条新数据

# b = model.remove({'name':'tianjing3'})
# for i in b:
#     print(i)
c = model.find()
for i in c:
    print(i)
