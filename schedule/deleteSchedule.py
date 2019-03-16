from helper import removeShcedule
from connection import create_connection
from makeSchedule import dayList
from showSchedule import showSchedule

def deleteSchedule() :

    id = int(input("Which activity number would you want to delete ? :"))

    conn = create_connection()
    isRemoved = removeShcedule(conn, id)

    if isRemoved :
        print("Success")
    else :
        print("Failed")

deleteSchedule()
