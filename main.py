from karatsuba import Karatsuba 
import datetime


def main():
    
    x = 10
    y = 20

    startTime = datetime.datetime.now()
    result = Karatsuba.multiply(x , y)
    endTime = datetime.datetime.now()
    print(x, " * " , y)
    print("Resutaldo Karatsuba: ", result)
    print("Tempo: ", (endTime - startTime), "\n")

    x = 32423
    y = 42345

    startTime = datetime.datetime.now()
    result = Karatsuba.multiply(x , y)
    endTime = datetime.datetime.now()

    print(x, " * " , y)
    print("Resutaldo Karatsuba: ", result)
    print("Tempo: ", (endTime - startTime), "\n")


    x = 23423423
    y = 423423423

    startTime = datetime.datetime.now()
    result = Karatsuba.multiply(x , y)
    endTime = datetime.datetime.now()

    print(x, " * " , y)
    print("Resutaldo Karatsuba: ", result)
    print("Tempo: ", (endTime - startTime), "\n")



    x = 3423094823049238904238098234
    y = 4234234234234023943909123423

    startTime = datetime.datetime.now()
    result = Karatsuba.multiply(x , y)
    endTime = datetime.datetime.now()

    print(x, " * " , y)
    print("Resutaldo Karatsuba: ", result)
    print("Tempo: ", (endTime - startTime), "\n")


    x = 3423094823049238904238098223482309483209840238409280374023
    y = 4234234234234023943909123423131231231928301280312

    startTime = datetime.datetime.now()
    result = Karatsuba.multiply(x , y)
    endTime = datetime.datetime.now()

    print(x, " * " , y)
    print("Resutaldo Karatsuba: ", result)
    print("Tempo: ", (endTime - startTime), "\n")

main()