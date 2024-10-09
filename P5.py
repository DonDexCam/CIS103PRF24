print('Table codes: A=add, S=Subtract, M=multiple, D=divide')
code=input('Select table code')
numb=float(input('enter a number'))
if code=='A':
    for x in range(1,11,1):
        answer=numb+x
        print(answer,'=', numb, '+', x)
else:
    if code=='S':
        for x in range(1,11,1):
            answer=numb-x
            print(answer, '=', numb, '-', x)
    else:
        if code=='M':
            for x in range(1,11,1):
                answer=numb*x
                print(answer, '--', numb, '*', x)
        else:
            if code=='D':
                for x in range(1,11,1):
                    answer=numb/x
                    print(answer, '=', numb, '/', x)
            else:
                print('unknown code')
print('program done')
