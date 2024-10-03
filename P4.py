name=input('Enter name')
lenname=len(name)
if(lenname==0):
    print('Name cannot be blank')
else:
    if name.isnumeric():
        print('Name must be alphabetic')
    else:
        if name.isspace():
            print('Name cannot be blank')
        else:
            if name.isalpha():
                print('Name is valid')
            else:
                print('Name must be alphabetic')
account=input('Enter account number')
lenacc=len(account)
if(lenacc==0):
        print('Account number cannot be blank')
else:
    if account.isspace():
        print('Account number must be 9 digits')
    else:
        if account.isnumeric():
            print('Account is valid')
        else:
            print('Account must be numeric')

pymt=input('Enter payment amount')
lenpymt=len(pymt)
if(lenpymt==0):
    print('Payment cannot be blank')
else:
    if pymt.isspace():
        print('Payment cannot be blank')
    else:
        pymt=float(pymt)
        if pymt<0:
            print('Payment cannot be negative')
        else:
            if pymt==0:
                print('Payment cannot be zero')
            else:
                print('valid')

