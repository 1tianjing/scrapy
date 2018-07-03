
import pymongo
import json


def main():
    mongoclient = pymongo.MongoClient('127.0.0.1',27017)



    #拿到mongodb里面的数据库
    db = mongoclient['BAIDULVYOU_TJ']
    #拿数据库中的集合
    LVYOU_TJ = db['LVYOU_TJ']
    while True:
        data = json.loads(data)
        LVYOU_TJ.insert(data)
        print(data)


if __name__ == '__main__':
    main()