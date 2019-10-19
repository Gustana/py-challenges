# * * * * * * * * * * *
# * *               * *
# *   *           *   *
# *     *       *     *
# *       *   *       *
# *         *         *
# *       *   *       *
# *     *       *     *
# *   *           *   *
# * *               * *
# * * * * * * * * * * *

# * * * * * * * * * *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# *       * *       *
# *     *     *     *
# *   *         *   *
# * *             * *
# * * * * * * * * * *

limit = int(input("masukkan batas :"))

border = int(limit/2)

start = 1
cons = 1

while(start <= limit) :
    i = 1
    j = limit

    while(i <= limit) :

        diff = (limit-start) + 1

        if start == 1 or start == limit or i == 1 or i == limit or i == start or i == diff:
            print("* ", end="")
        else :
            print("  ", end="")

        i+=1

    print("")

    start+=1