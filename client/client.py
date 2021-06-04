import socket

s=socket.socket()

host=input(str("Enter the host address of sender >> "))
port=8080

s.connect((host,port))
print("connected to the sender")

fileName=input(str("Enter the name for incoming file >>"))
file=open(fileName,'wb')
fileData=s.recv(1024)
file.write(fileData)

file.close()
print("File Recieved Successfully")
