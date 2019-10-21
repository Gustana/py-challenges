height = int(input("Insert height :")) #5

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

limit = 1

while (limit<=height) :
    star = limit
    space = height

    while (space >= limit) :
        print(" ", end="")
        space-=1

    while (star >= 1) :
        print("* ", end="")
        star-=1

    print("")

    limit+=1