from helper import insertSchedule
from connection import create_connection

dayList = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def makeSchedule() :
    i = 1
    while i<7 :
        print(i, end=".")
        print(dayList[i-1], sep='\n')
        i+=1

    day = int(input("Select day : "))
    time = input("Insert time :")
    activity = input("What do you want to do ? :")

    schedule = (activity, time, day)

    conn = create_connection()
    with conn :
        query = insertSchedule(conn, schedule)
        if query :
            print("Success")
        else :
            print("Failed")

    