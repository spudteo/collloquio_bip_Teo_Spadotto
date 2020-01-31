import sys

##testato su pycharm
###complessità lineare
###input su linea di comando,
##un numero dietro l'altro con uno spazio come divisorio
##per testare se no decommentare e incollare
#array = [-3,-2,2,5,-6,8,-3]


def maxsum(array):

    #controllo se è vuoto
    if len(array) == 0 :
        return "error empty input"

    max_sum = -sys.maxsize - 1
    max = 0
    start = 0
    end = 0
    s = 0

    for i in range(0 ,len(array)):

        max += array[i]

        if max_sum < max:
            max_sum = max
            start = s
            end = i
        if max < 0:
            max = 0
            s = i+ 1

    sub_Array = array[start:end+1]
    return sub_Array, max_sum


#prova leggendo dallo stdin e printa il risultato, input tutto in una riga separata da spazio dopo l'invio ha preso input
array = [int(i) for i in input().split()]
print(maxsum(array))


