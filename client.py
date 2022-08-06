import socket
import sys
IP = '127.0.0.1'
Port = 5555

user = str(input("Your Name if you please! : ")).encode()
password = str(input("Your Pin to allow you access! : ")).encode()
balance = str(input("How much balance is in your account?? ")).encode()
tran = str(input("What process do you want to do (deposit,withdraw) ? : ")).encode()
amount = str(input("Enter the amount please to do what you want was a withdrawal or deposit : ")).encode()




def main():
 odaysocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
 odaysocket.sendto(user,(IP,Port))
 odaysocket.sendto(password,(IP,Port))
 odaysocket.sendto(balance,(IP,Port))
 odaysocket.sendto(tran,(IP,Port))
 odaysocket.sendto(amount,(IP,Port))
 rec,add=odaysocket.recvfrom(1024)
 print("Remaining amount in your account:")
 print(rec.decode())
 
if __name__ == "__main__":
    if user.decode() == '' or password.decode() == '' or tran.decode() == '' :
       print("Enter your credintial corcitly ")
       quit()
    else :
      main()
   
