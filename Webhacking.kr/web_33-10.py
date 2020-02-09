ip=""
lastIP=""
print (len(ip))
i=0
#increase len(ip) value when doing 'for' cycle
while(i!=len(ip)+1):
    if i<10:
        lastIP=ip
        ip=ip.replace(str(i), str(ord(str(i))))
    elif i>=10 and i<20:
        lastIP=ip
        ip=ip.replace(str(i), str(ord('1')))
    elif i>=20 and i<30:
        lastIP=ip
        ip=ip.replace(str(i), str(ord('2')))
    elif i>=30 and i<40:
        lastIP=ip
        ip=ip.replace(str(i), str(ord('3')))
    print("[{}] {} -> {}".format(i, lastIP, ip))
    i+=1

print(ip)
ip=ip.replace(".", "")
ip=ip[0:10]
answer=int(ip)*2
answer=int(ip)/2
answer=str(answer).replace(".", "")
print(answer)
print(answer+"_"+ip+".php")