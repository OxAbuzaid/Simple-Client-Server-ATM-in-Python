import socket
import sys 

 
localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

username = ['ayham,khalid,mohammad']
passwd   =  str(1234) 
tran_deposit =  'deposit'
tran_withdraw = 'withdraw'
money = 1000

try:
   socket1  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   socket1.bind((localIP, localPort))
except socket.error:
   print("Faild to open socket")
except socket.herror :
   print("Faild to open socket ") 
except socket.gaierror:
   print("Faild to open socket ") 
except socket.timeout:
   print("Faild to open socket ") 
 
       
print("[+] listening on IP {} Port {}".format(localIP , localPort))
print("Team members: \nAyham Doumi \nMohammad Aldalki \nKhalidAbuzaid")      
 



while True:

    data_user  , address_user   = socket1.recvfrom(bufferSize)
    data_passwd, address_passwd = socket1.recvfrom(bufferSize)
    data_tran ,  address_tran   = socket1.recvfrom(bufferSize)
    data_amount, address_amount = socket1.recvfrom(bufferSize)
    if data_passwd.decode() == passwd :
       
       if data_tran.decode() == tran_deposit or data_tran.decode() == tran_withdraw :
           if data_tran.decode() == tran_deposit :
               newmoney =  money + int(data_amount.decode())
               print("you have an deposit process and your amount now is :")
               print(newmoney)
               socket1.sendto(str.encode(str(money)),address_tran) 
           if data_tran.decode() == tran_withdraw:
              newmoney =  money - int(data_amount.decode())
              print("you have an deposit process and your amount now is :")
              print(newmoney)
              socket1.sendto(str.encode(str(money)),address_tran)
           
       else:
          print("Enter Correct Process")
    else :
      print("Enter Correct PIN")
      
      
