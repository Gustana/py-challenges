def insertSchedule(conn, schedule) :
    query = ''' INSERT INTO schedule(activity, time, day) 
            VALUES(?, ?, ?)'''

    cursor = conn.cursor()
    cursor.execute(query, schedule)
    return True