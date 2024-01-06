import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable
from general import *
from queries import *
import settings

while(1):
    tmp = sp.call('clear', shell=True)

    try:
        # con = connect_to_sever()
        settings.init()
        tmp = sp.call('clear', shell=True)
        if(settings.con.open): 
            print("\033[92m" + "Connected to sql server" + "\033[0m")
        else:
            print("Failed to connect")
    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        break 

    show_catgories()
    choice = int(input("Enter your choice> "))

    if choice == 4:
        break 
    else:
        show_options(choice)
        sub_choice = int(input("Enter your choice> "))
        # cur = settings.con.cursor()
        # with settings.con.cursor() as cur:
        tmp = sp.call('clear', shell=True)
        try:
            dispatch(choice, sub_choice)
        except pymysql.Error as e:
            print("\033[91m" + f"SQL error: {e}" + "\033[0m")
        tmp = input("Enter any key to CONTINUE>")   

    