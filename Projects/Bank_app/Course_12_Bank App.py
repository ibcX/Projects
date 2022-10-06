import uuid
from datetime import datetime

ADD_CLIENT_COMMAND = 'add_client'
READ_CLIENT_BALANCE = 'read_balance'
HELP_COMMAND = 'help'
LOGIN_COMMAND = 'login'
LOGOUT_COMMAND = 'logout'
MODIFY_BALANCE = 'modify_balance'
TRANSFER_MONEY = 'transfer_money'
EXIT_COMMAND = 'exit'
IS_USER_LOGGED_IN = False
ACCOUNT_STATEMENT = 'account_statement'

def login(user, password):
    file = open('auth.txt', 'r')  # user,passwor
    for line in file:
        line = line.strip("\n")
        data = line.split(',')
        user_name = data[0]
        user_password = data[1]
        if user == user_name and password == user_password:
            file.close()
            return True
    file.close()
    return False


def must_login():
    global IS_USER_LOGGED_IN
    if IS_USER_LOGGED_IN:
        print("You are already logged in!")
    else:
        print("You need to log in!")
        user_name = input('Please insert username: ')
        user_password = input('Please insert password: ')

        if login(user_name, user_password):
            IS_USER_LOGGED_IN = True
            print("User has logged in!")
        else:
            print("Try again, username/password incorrect!")


def logout():
    global IS_USER_LOGGED_IN
    IS_USER_LOGGED_IN = False
    print("You have been logged out!")


def start_create_client_procedure():
    print("Add new client")
    file = open('clients.txt', 'a')
    client_id = uuid.uuid4()
    client_name = input('Client name: ')
    client_phone = input('Client phone: ')
    client_town = input('Client town: ')
    file.write(f'{client_id},{client_name},{client_phone},{client_town} \n')
    file.close()
    file = open('accounts.txt', 'a')
    file.write(f'{client_id},{0},RON\n')
    file.close()
    print(f"The new client has been added successfully: {client_name},{client_phone}, {client_town}")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open(f'{client_id}.txt', 'w')
    file.write(f"""
________________________________________________________________________________________________
                                   Account statement                                             
                                                                                Titulescu Bank
                                                                                Banca IT-istilor
Client:
Name: {client_name}
Phone number: {client_phone}
Town: {client_town}
________________________________________________________________________________________________

{date_time}     Balance: {0} RON\n
""")
    file.close()

print('''
    Welcome to the Titulescu Bank!
    If you don't know hou to use the application please use the "help" command.
''')


def retrieve_client_id():
    print("Specify client's information")
    client_name = input("Client name: ")
    client_phone = input("Client phone: ")
    file = open('clients.txt', 'r')
    client_id = None
    for line in file:
        client_data = line.split(',')
        client_data_name = client_data[1]
        client_data_phone = client_data[2]
        if client_name == client_data_name and client_phone == client_data_phone:
            client_id = client_data[0]
    file.close()
    return client_id

def retrieve_client_name(client_id):
    file = open('clients.txt', 'r')
    client_data_name = None
    for line in file:
        client_data = line.split(',')
        if client_id == client_data[0]:
            client_data_name = client_data[1]
    file.close()
    return client_data_name


def get_all_accounts():
    accounts_file = open('accounts.txt', 'r')
    all_accounts = accounts_file.readlines()
    accounts_file.close()
    return all_accounts


def read_account_balance(client_id):
    all_accounts = get_all_accounts()
    for account in all_accounts:
        account_data = account.split(',')
        if client_id == account_data[0]:
            print(f"Client's account has {account_data[1]}{account_data[2]}")
            return float(account_data[1])


def update_balance(client_id, transfer_amount, client):
    accounts = get_all_accounts()
    for index, account in enumerate(accounts):
        account_data = account.split(',')
        if client_id == account_data[0]:
            new_account_balance = float(account_data[1]) + transfer_amount
            accounts[index] = f'{account_data[0]},{new_account_balance},{account_data[2]}'
            print(f"{client}'s balance has been updated successfully!\n The new balance is: {new_account_balance} {account_data[2]}")

    file = open('accounts.txt', 'w')
    file.writelines(accounts)
    file.close()
    return new_account_balance



def transfer_money():
    sender_client_id = retrieve_client_id()
    if sender_client_id:
        sender_account_balance = read_account_balance(sender_client_id)
        receiver_client_id = retrieve_client_id()
        if receiver_client_id:
            transfer_amount = float(input('Please enter the amount you want to send: '))
            if transfer_amount > sender_account_balance:
                print("Not enough money!")
            elif transfer_amount <= 0:
                print("You can not transfer negative or zero amounts")
            else:
                date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                receiver_new_balance = update_balance(receiver_client_id, transfer_amount, "Receiver")
                sender_new_balance = update_balance(sender_client_id, -transfer_amount, "Sender")
                file = open('money_transfer_history.txt', 'a')
                file.write(f'{date_time},{sender_client_id},{receiver_client_id},{-transfer_amount},RON,{transfer_amount},RON\n')
                file.close()
                print(f"The money transfer history has been updated.")

                receiver_name = retrieve_client_name(receiver_client_id)
                sender_name = retrieve_client_name(sender_client_id)
                file = open(f'{receiver_client_id}.txt', 'a')
                file.write(f'{date_time}    Transfer from {sender_name} {transfer_amount} RON\nNew balance: {receiver_new_balance}\n\n')
                file.close()

                file = open(f'{sender_client_id}.txt', 'a')
                file.write(f'{date_time}    Transfer to {receiver_name} {-transfer_amount} RON\nNew balance: {sender_new_balance}\n\n')
                file.close()


        else:
            print("There is no such client in bank's database!")
    else:
        print("There is no such client in bank's database!")

def account_statement():
    client_id = retrieve_client_id()
    file = open(f"{client_id}.txt", "r")
    for line in file:
        print(line)
    print("""
__________________________________________________________________________________________
End of report\n""")
    file.close()

while True:
    user_command = input('Please specify your command: ').lower()
    if user_command == EXIT_COMMAND:
        break
    elif user_command == HELP_COMMAND:
        print('''
        This application can do a multitude of things based on the command that was imputed.
        Commands available :
            - login             Logs you in the bank's system      
            - add_client        Starts process for adding new client
            - read_balance      Shows client's account balance
            - logout            Logs you out
            - modify_balance    Modifies client's account balance
            - transfer_money    Begins money transfer between two clients of our bank
            - account_statement Shows the account statement of a client
            - exit              Exit the application   
        ''')
    elif user_command == LOGIN_COMMAND:
        must_login()
    elif user_command == LOGOUT_COMMAND:
        logout()
    else:
        if not IS_USER_LOGGED_IN:
            print("You are not logged in, please use -login command to do so!")
            continue
        else:
            if user_command == ADD_CLIENT_COMMAND:
                start_create_client_procedure()
            elif user_command == READ_CLIENT_BALANCE:
                client_id = retrieve_client_id()
                if client_id:
                    read_account_balance(client_id)
                else:
                    print('User does not exist in the system.')

            elif user_command == MODIFY_BALANCE:
                client_id = retrieve_client_id()
                if client_id:
                    read_account_balance(client_id)
                    transfer_amount = float(input("Please enter the amount you want to transfer: "))
                    new_account_balance = update_balance(client_id, transfer_amount, "Client")
                    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    file = open(f'{client_id}.txt', 'a')
                    file.write(
                        f'{date_time}    Account credited with {transfer_amount} RON\nNew balance: {new_account_balance}\n\n')
                    file.close()
                else:
                    print("Client does not exist in our system.")

            elif user_command == TRANSFER_MONEY:
                transfer_money()

            elif user_command == ACCOUNT_STATEMENT:
                account_statement()

            else:
                print("Wrong command! To show the available commands please write -help.")



# FOR HOMEWORK
# Pt Transfer Bancar intre useri:
# - Update balanta useri
# - Sa existe suma respectiva la platitor
# - Trebuie un history de money transfer
# - Trebuie ca primitorul sa existe si sa aiba account


# 1. Identificam platitor
# 2. Citim balanta
# 3. Verificam suma de transfer vs ce are in cont(aka daca isi permite sa faca transferul)
# 4. Daca isi perimte mergem la next stepts daca nu print ca nu ai bani pls add more
# 5. Identificare beneficiar
# 6. Daca beneficiar exista mergem to next steps else print nu putem transfera nu are contul la noi
# 7. Modify balance platitor (scadem din balance)
# 8. Modify balance beneficiar (adaugam in balance)
# 9. Inresitarea tranzactiei in money_transfer_history
#     Money transfer history txt file
# platitor_id,beneficiar_id,suma_iesita_din_cont_platitor,moneda,suma_intrata_in_cont_beneficiar,moneda
