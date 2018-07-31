import pin

from ring import Ring
from tower import Tower
test = Tower(3)
print(test.pins[2])
print((test.pins[1].rings))
print((test.pins[0].rings))


#def hanoi(n, A, B, C):
 # if(n > 0):
#    hanoi(n-1, A, C, B)
#    print ("Mova o disco " + str(n) + " de " + A + " para " + B)
#    hanoi(n-1, C, B, A)
#hanoi(3, "A","B","C" )
