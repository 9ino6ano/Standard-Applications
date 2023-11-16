import socket
hostname=socket.gethostname()
IP=socket.gethostbyname(hostname)

print("Your Device name is: ",hostname)
print("Your Device IP Address is: ",IP)

