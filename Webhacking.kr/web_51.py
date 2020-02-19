import hashlib;a=(hashlib.md5('123456789'.encode())).digest();

def findString():
    for i in range(1000000, 100000000):
        hashString=hashlib.md5(str(i).encode()).digest();print("(+) [{}] -> [{}]".format(i, hashString))
        if ("'='".encode() in hashString):print(i);break;

if __name__=="__main__":
    findString()