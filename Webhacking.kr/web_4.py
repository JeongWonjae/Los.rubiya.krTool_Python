import hashlib

def encodingRepeat(string):
    str=string
    result=hashlib.sha1(str.encode("utf-8"))

    for i in range(0, 499):
        result=hashlib.sha1(result.hexdigest().encode("utf-8"))
        #print(result.hexdigest())

    return result.hexdigest()

def getHash(start, end):
    file = open("rainbowTable2.txt", "w")

    for index in range(start, end):
        result=encodingRepeat(str(index)+"salt_for_you")

        file.write(str(index) + "salt_for_you -> " + result + "\n")
        print(str(index)+" = "+result)

    file.close()

#__main__
getHash(30000001, 60000000)