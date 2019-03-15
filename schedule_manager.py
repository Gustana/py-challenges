scheduleList = []
dayList = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def createSchedule() :
    num = 0
    while num <= 6 :
        print(num+1, end=". ")
        print(dayList[num], sep='\n')
        num+=1

    day = int(input("Select day :"))
    schedule = input("What you want to do ? :")
    scheduleList[day].append(schedule)

createSchedule()

sadf