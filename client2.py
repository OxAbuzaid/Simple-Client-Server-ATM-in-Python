import socket
import sys
IP = '127.0.0.1'
Port = 20001

user = str(input("Enter Your Name : ")).encode()
password = str(input("Your PIN : ")).encode()
transection = str(input("What process do you want to do ? : ")).encode()
amount = str(input("Enter the amount please  : ")).encode()




def main():
 s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
 s.sendto(user,(IP,Port))
 s.sendto(password,(IP,Port))
 s.sendto(transection,(IP,Port))
 s.sendto(amount,(IP,Port))
 rec,add=s.recvfrom(1024)
 print(rec.decode())
 
if __name__ == "__main__":
    if user.decode() == '' or password.decode() == '' or transection.decode() == '' :
       print("Enter your credintial corcitly ")
       quit()
    else :
      main()
   
