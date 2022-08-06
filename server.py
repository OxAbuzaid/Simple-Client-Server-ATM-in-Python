import socket
import sys 

# socket information 
localIP     = "127.0.0.1"
localPort   = 5555
bufferSize  = 1024
# userinformation 
username = 'oday'
passwd   =  str(1111)  # socket.sendto(msg,socket)
tran_deposit =  'deposit'
tran_withdraw = 'withdraw'


error = "Enter corrct transaction".encode()
error1 = "Enter corrct credintails ".encode()
try:
   odaysocket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   odaysocket.bind((localIP, localPort))
except socket.error:
   print("Faild to open socket")
except socket.herror :
   print("Faild to open socket ") 
except socket.gaierror:
   print("Faild to open socket ") 
except socket.timeout:
   print("Faild to open socket ") 
 
       
print("[+] listening on Port {} IP {} #####".format(localPort,localIP))


# Listen for incoming datagrams

while True:

    data_user  , address_user   = odaysocket.recvfrom(bufferSize)
    data_passwd, address_passwd = odaysocket.recvfrom(bufferSize)
    data_balance, address_balance = odaysocket.recvfrom(bufferSize)
    data_tran ,  address_tran   = odaysocket.recvfrom(bufferSize)
    data_amount, address_amount = odaysocket.recvfrom(bufferSize)
    if data_user.decode() == username and data_passwd.decode() == passwd :
       print("The Balance in your account is:",int(data_balance.decode()))  
       if data_tran.decode() == tran_deposit or data_tran.decode() == tran_withdraw :
           if data_tran.decode() == tran_deposit :
               money =  int(data_balance.decode()) + int(data_amount.decode())
               print("An amount has been deposited into your account and the amount in your account is:")
               print(money)
               odaysocket.sendto(str.encode(str(money)),address_tran) # odaysocket.sendto(money , address)
           if data_tran.decode() == tran_withdraw:
              money =  int(data_balance.decode()) - int(data_amount.decode())
              print("An amount has been withdrawn from your account and the amount in your account is:")
              print(money)
              odaysocket.sendto(str.encode(str(money)),address_tran)
           
       else:
          odaysocket.sendto(error,address_tran)
    else :
      odaysocket.sendto(error1,address_user)
      
      
