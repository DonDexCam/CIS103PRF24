def miles_to_k():
    m=float(input('enter miles->'))
    k=m*1.609344
    print('kilometers is:',k)
    return
def temp():
    F=float(input('enter Fahrenheit->'))
    C=(F-32)*5/9
    print('Celius is',C)
    return
def weight():
    lb=float(input('Enter Pounds->,'))
    kg=lb*0.45359237
    print('Kilograms is',kg)
    return


def main():
    miles_to_k()
    temp()
    weight()


    return
main()
print('done')
