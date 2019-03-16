def insertSchedule(conn, schedule) :
        query = ''' INSERT INTO schedule(activity, time, day) 
            VALUES(?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(query, schedule)
        return True

def selectSchedule(conn, query) :
        cursor = conn.cursor()
        cursor.execute(query)
        
        rows = cursor.fetchall()

        return rows

def removeShcedule(conn, id) :
        query = ''' DELETE FROM schedule WHERE id = ? '''
        cursor = conn.cursor()
        cursor.execute(query, (id,))

        return True
                