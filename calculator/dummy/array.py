
#1 2 
#3 4
#5 6

arrays = [[6,7],[8,9],[10,11]]

i, j = 0,0
while i < 3 :
    while j < 1 :
        print(arrays[i][j], end=" ")
        print(arrays[i][j+1])
        j+=1
    j=0
    i+=1