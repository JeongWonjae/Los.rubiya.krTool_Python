import socket

utf="utf-8"
host="0.0.0.0"
size=1024

def openServer(host, port, size):
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(0)
    print("[+] Create server socket : {}".format(port))

    while True:
        client_socket,addr=server_socket.accept()
        print("[+] Connect with client. :{}".format(port))
        data=client_socket.recv(size)
        decode_data=data.decode(utf)
        print("[+] [{}] message : {}".format(addr, decode_data))

        #send_data="thisis send data"
        #send_data_byte=send_data.encode(utf)
        #client_socket.send(send_data_byte)

    client_socket.close()
    server_socket.close()

if __name__=='__main__':
    openServer(host, 7777, size)

#port check -> netstat -ano
#port close -> taskkill /f /pid {number}
