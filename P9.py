def miles_to_k():
    try:
        m=float(input('enter miles->'))
        k=m*1.609344
        print('kilometers is:',k)
    except:
        print('data error')
    return
def temp():
    try:
        F=float(input('enter Fahrenheit->'))
        C=(F-32)*5/9
        print('Celius is',C)
    except:
        print('data error')
    return
def weight():
    try:
        lb=float(input('Enter Pounds->,'))
        kg=lb*0.45359237
        print('Kilograms is',kg)
    except:
        print('data error')
    return


def main():
    answer='yes'
    while answer=='yes':
        miles_to_k()
        temp()
        weight()
        answer=input('enter yes or no')


    return
main()
print('done')
