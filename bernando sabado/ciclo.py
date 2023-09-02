
import random

vidas= 5

puntos= 0

#si sale cero pierde una vida

#si se genera cualquier otro numero dentro  un rago establecido, gana punto



while vidas !=0:

    num= random.randint(0,9)

    if num != 0:
        puntos+=1
        print ("tienes " ,  puntos, "puntos")

    else:
        vidas-=1
        print ("te quedan ", vidas , "vidas") 
