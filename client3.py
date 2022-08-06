
import socket


def Main():

    host = '127.0.0.1'
    port = 55023

    teamsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    teamsocket.connect((host, port))

    while True:
        
        ans = input('\nWhat would you like to do?'
                    '\n1: balance'
                    '\n2: Withdrawal'
                    '\n3: Deposit'
                    '\nquit: End Connection'
                    '\n your Choice:')
        if ans == '1':
            teamsocket.send(ans.encode('ascii'))
            data = teamsocket.recv(1024)
            print('\nbalance Right Now = :', str(data, 'utf8'))
            continue
            
        if ans == '2':
            teamsocket.send(ans.encode('ascii'))
            withdraw = input('\n How much do you want to withdraw from your account?: ')
            teamsocket.send(withdraw.encode('ascii'))
            data = teamsocket.recv(1024)
            if data == b'No':
                print("\nNot enough Money.")
            else:
                print('\nBalance after pervious process :', str(data, 'utf8'))
            continue
            
        if ans == '3':
            teamsocket.send(ans.encode('ascii'))
            deposit = input('\n How much do you want to deposit in your account? : ')
            teamsocket.send(deposit.encode('ascii'))
            data = teamsocket.recv(1024)
            print('\nBalance after pervious process  :', str(data, 'utf8'))
            continue
        
        if ans == 'quit':
            print("\nEnding Connection")
            break
        else:
            print("\nNot a valid input, try again.")
            continue
    # close the connection
    teamsocket.close()


if __name__ == '__main__':
    Main()
