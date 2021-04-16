import random
import sys
import json
import pyperclip
from encriptit import encrypt_message, decrypt_message

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
charecter = ["!","@","#","$","%","&","*"]
numbers = [0,1,2,3,4,5,6,7,8,9]

def GenPassword():
    Password = ""
    account = input("what is the password for: ")
    char = int(input("how long do you want the password: "))
    for i in range(1,char):
        Rchar   = random.choice(charecter)
        Ralpha  = random.choice(alphabet)
        Rnum    = random.choice(numbers)
        Password = Password + Rchar + Ralpha + str(Rnum)
    Default_pass = input("Main Passowrd: ")
    Pfile = open(".dontopen.log")
    x = Pfile.read()
    Pfile.close()
    if (Default_pass == decrypt_message(x)):
        E = encrypt_message(Password)
        DP = E.decode()
        rPass = {account:DP}
        Writepass(rPass)
    else:
        print("wrong Password!")
def Writepass(passw):
    outfile = open("main.json", 'r+')
    data = json.load(outfile)
    data.update(passw)
    outfile.seek(0)
    json.dump(data, outfile)

def Copypass():
    acc = input("what is the name of the account(type the correct account): ")
    outfile = open("main.json")
    data = json.load(outfile)
    for account, password in data.items():
        if acc == account:
            Default_pass = input("Main Passowrd: ")
            Pfile = open(".dontopen.log")
            x = Pfile.read()
            Pfile.close()
            if (Default_pass == decrypt_message(x)):
                pyperclip.copy(decrypt_message(password))
                print("copied")
            else:
                print("Wrong Password!")
def Cridit():
    print("""
         _ __  _ __ __ _ _ __   __ ___   __      ___ ___   __| (_)_ __   __ _ 
| '_ \| '__/ _` | '_ \ / _` \ \ / /____ / __/ _ \ / _` | | '_ \ / _` |
| |_) | | | (_| | | | | (_| |\ V /_____| (_| (_) | (_| | | | | | (_| |
| .__/|_|  \__,_|_| |_|\__,_| \_/       \___\___/ \__,_|_|_| |_|\__, |
|_|                                                             |___/ 

     """)
    print("I am the creater of this product \n for an questions come to https://github.com")

def GENMAINPASS():
    Default_pass = input("Main Passowrd: ")
    Pfile = open(".dontopen.log")
    x = Pfile.read()
    Pfile.close()
    if (Default_pass == decrypt_message(x)):
        MAINPASS = input("what is the new password: ")
        outfile = open(".dontopen.log", "r+")
        outfile.seek(0)
        outfile.truncate()
        x = encrypt_message(MAINPASS)
        outfile.write(x.decode())
        outfile.close()
    else:
        print("wrong Password!") 

def Instruction():
    todo = input("Command: ")
    if todo == "--h":
        print("cppass")
        print("newpass")
        print("exit")
        print("credit")
        print("generate password")
    elif todo == "newpass":
        GenPassword()
    elif todo == "cppass":
        Copypass()
    elif  todo == "exit":
        sys.exit()
    elif todo == "credit":
        Cridit()
    elif todo == "generate password":
        GENMAINPASS()
while True:
    Instruction()
