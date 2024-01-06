import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable
from general import *
from queries import *

def init():
    global con 
    global cur 
    con = pymysql.connect(host='localhost',
                        port=3306,
                        user="root",
                        password="rootroot",
                        db='icpc',
                        cursorclass=pymysql.cursors.DictCursor)
    cur = con.cursor()
