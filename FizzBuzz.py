# -*- coding: utf-8 -*-
#Naloga v nalogi. FizzBuzz ter stringi z malimi ter velikimi črkami

#Uporabnik naj vnese število med 1 in 100
#Program naj začne šteti do te izbrane številke (in izpiše vsako številko v terminalu).
#V primeru da je številka deljiva s 3, naj namesto številke v terminalu izpiše "fizz".
#V primeru da je številka deljiva s 5, naj namesto številke v terminalu izpiše "buzz".
#V primeru da je številka deljiva tako s 3, kot s 5, naj namesto številke v terminalu izpiše "fizzbuzz".

for num in range(1, 100+1):

    if num % 3 == 0 and num % 5 == 0:
        print str.lower("FIZZBUZZ")

    # Sem imel kar težave saj sem šel po navodilih kjer je FizzBuzz na zadnjem mestu.
    # če dam v kodi FizzBuzz na zadnje mesto tega sploh ne zazna. Zakaj?

    elif num % 3 == 0:
        print str.upper("fizz")

    elif num % 5 == 0:
        text = "BuZZ"
        print text.lower()

    else:
        print num




