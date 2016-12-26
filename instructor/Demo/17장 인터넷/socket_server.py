# -*- coding:cp949 -*- 
import socket

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)  #접속이 있을 때 까지 기다린다.
conn, addr = s.accept()  #접속을 승인한다.
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break;
    conn.send(data)   #받은 데이터를 그대로 클라이언트에 전송한다.
conn.close()
