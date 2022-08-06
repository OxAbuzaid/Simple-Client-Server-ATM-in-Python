
import socket
from _thread import *
import threading

print_lock = threading.Lock()

balance = 1000

def threaded(M):
    global balance
    while True:

        data = M.recv(1024)
        if not data:
            print('GoodBye')

     
            print_lock.release()
            break

        
        if data == b'1':
            
            print("Your Balance :", balance)
            M.send(bytes(str(balance), 'utf8'))
        
        if data == b'2':
            withdrawal = M.recv(1024)
            print("Withdraw: ", str(withdrawal, 'utf8'))
           
            if int(withdrawal) < balance:
                balance = balance - int(withdrawal)
                print("Your Balance Right Now: ", balance)
                M.send(bytes(str(balance), 'utf8'))
            else:
                print("You don't have this money!!.")
                M.send(bytes("No", 'utf8'))
        
        if data == b'3':
            deposit = M.recv(1024)
            print("Deposit: ", str(deposit, 'utf8'))
            balance = balance + int(deposit)
            print("Your Balance Right Now: ", balance)
            M.send(bytes(str(balance), 'utf8'))
        
    M.close()


def Main():
    host = ""

    
    port = 55023
    teamsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    teamsocket.bind((host, port))
    print("socket binded to port", port)

    
    teamsocket.listen(5)
    print("socket is listening")

    
    while True:
        
        M, addr = teamsocket.accept()

       
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        
        start_new_thread(threaded, (M,))
    teamsocket.close()


if __name__ == '__main__':
    Main()
