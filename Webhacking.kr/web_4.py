import hashlib

afterHash="88e065fb59a3c53e523a2a6754a6d89a26f6dcad"
sha=hashlib.sha1()

def getHash(start, end):
    file = open("rainbowTable.txt", "w")

    for index in range(start, end):
        beforeHash = (str(index) + "salt_for_you").encode("utf-8")

        for i in range(0, 500):
            sha.update(beforeHash)

        file.write(str(index)+"->"+sha.hexdigest()+"\n")
        print("(+) ", beforeHash.decode("utf-8"), " -> ", sha.hexdigest())

        if (sha.hexdigest() == afterHash):
            print("(+) Find!")
            break

    file.close()

#__main__
getHash(40000000, 50000000)