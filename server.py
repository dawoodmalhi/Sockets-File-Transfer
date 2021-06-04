import socket

s=socket.socket()

host=socket.gethostname()
port=8080

s.bind((host, port))
s.listen(1)

print("host address of server is: ", host)
print("Waiting for incomming connection ...")

con, addr=s.accept()
print(addr, " has connected to the server")

fileName=input(str("Enter the name of file >> "))
file=open(fileName,'rb')
fileData=file.read(1024)

con.send(fileData)
file.close()
con.close()
print("File has been sent successfully")

