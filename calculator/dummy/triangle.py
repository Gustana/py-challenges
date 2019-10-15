# num = 600851475143

# devider = 1

# result = 0

# while(num % devider != 0) :
#     result = num/devider
#     print(result)

#     devider+=1


import datetime as dt

visit_date = dt.datetime.strptime("10", "%H")

visit_date = dt.datetime.strftime(visit_date, "%I:%S %p")

print(visit_date)