from connection import create_connection
from helper import selectSchedule
from prettytable import PrettyTable
import makeSchedule

def showSchedule() :

    query = ''' SELECT id, time, day, activity FROM schedule '''

    conn = create_connection()

    results = selectSchedule(conn, query)

    table = PrettyTable(['No', 'Time', 'Day', 'Activity'])

    for result in results :
        table.add_row([result[0], result[1], makeSchedule.dayList[result[2]], result[3]])

    print(table)
showSchedule()