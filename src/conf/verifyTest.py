import os
import time

import dotenv

dotenv.load_dotenv()

username = os.getenv('username')
password = os.getenv('password')

def verifyTest(username, password):
    os.system('clear')
    def firstUser():
        print("""
   \033[01;34m┌─────────────────────────────────────────────┐
     \033[02;34m▒█▀▀█ █▀▀█ █▀▀▄ █░░ █▀▀█ █▀▀ █░█
     \033[02;34m▒█▄▄█ █▄▄█ █░░█ █░░ █░░█ █░░ █▀▄
     \033[02;34m▒█░░░ ▀░░▀ ▀▀▀░ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀░▀\n\n
     \033[00;34mUser name \033[0m:\n
     \033[00;34mPass word \033[0m:\n\n
   \033[01;34m└─────────────────────────────────────────────┘
   """)
        global firstUsername
        os.system('tput cnorm')
        os.system('tput cup 7')
        firstUsername = input('\r\t\t \033[0;1m')
        os.system('tput civis')
        while firstUsername == '':
            os.system('tput cup 11')
            print('\r\t\t\t\033[31;1mUser required!')
            time.sleep(0.3)
            os.system('clear')
            firstUser()
        else:
            while firstUsername != username:
                os.system('tput cup 11')
                # os.system('tput civis')
                print('\r\t\t\t\033[31;1mUser incorrect!')
                time.sleep(0.3)
                os.system('clear')
                firstUser()
            else:
                pass
            pass

        def firstPass():
            os.system('clear')
            print("""
   \033[01;34m┌─────────────────────────────────────────────┐
     \033[02;34m▒█▀▀█ █▀▀█ █▀▀▄ █░░ █▀▀█ █▀▀ █░█
     \033[02;34m▒█▄▄█ █▄▄█ █░░█ █░░ █░░█ █░░ █▀▄
     \033[02;34m▒█░░░ ▀░░▀ ▀▀▀░ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀░▀\n\n
     \033[00;34mUser name \033[0m: {}\n
     \033[00;34mPass word \033[0m:\n\n
   \033[01;34m└─────────────────────────────────────────────┘
   """.format(firstUsername))
            global firstPassword
            os.system('tput cnorm')
            os.system('tput cup 9')
            firstPassword = input('\r\t\t \033[0;1m')
            os.system('tput civis')
            while firstPassword == '':
                os.system('tput cup 11')
                print('\r\t\t\t\033[31;1mPass required!')
                time.sleep(0.3)
                firstPass()
            else:
                while firstPassword != password:
                    os.system('tput cup 11')
                    print('\r\t\t\t\033[31;1mPass incorrect!')
                    time.sleep(0.3)
                    firstPass()
                else:
                    sucess()
                    os.system('tput cup 19')
                    print('Sucessfuly Ok')
                    os.system('tput cnorm')
                    exit()
        firstPass() 
    firstUser()


def sucess():
    steps = ['[□□□□□□]','[\033[01;95m■\033[0m□□□□□]','[□\033[01;96m■\033[0m□□□□]','[□□\033[01;95m■\033[0m□□□]','[□□□\033[01;96m■\033[0m□□]','[□□□□\033[01;95m■\033[0m□]','[□□□□□\033[01;96m■\033[0m]','[\033[01;95m■\033[0m□□□□□]','[□\033[01;96m■\033[0m□□□□]','[□□\033[01;95m■\033[0m□□□]','[□□□\033[01;96m■\033[0m□□]','[□□□□\033[01;95m■\033[0m□]','[□□□□□\033[01;96m■\033[0m]','[ \033[01;96mDone\033[0m ]']

    for step in steps:
        os.system('tput cup 17')
        print('\r\033[0m    Loading... {}'.format(step))
        time.sleep(0.1)

#verifyTest(username, password)
