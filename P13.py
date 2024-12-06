#Donavan Bryant using dictionary to convert numbers to roman numerals
def main():
    #Set up dictionary
    Roman_Numerals = {1:'I',
                      2:'II',
                      3:'III',
                      4:'IV',
                      5:'V',
                      6:'VI',
                      7:'VII',
                      8:'VIII',
                      9:'IX',
                      10:'X',
                      11:'XI',
                      12:'XII',
                      13:'XIII',
                      14:'XIV',
                      15:'XV',
                      16:'XVI',
                      17:'XVII',
                      18:'XVIII',
                      19:'XIX',
                      20:'XX',
                      21:'XXI',
                      22:'XXII',
                      23:'XXIII',
                      24:'XXIV'}
    print('Roman Numerals')
    print(Roman_Numerals)
    a=int(input('Enter a number:'))
    while a>0:
        if a in Roman_Numerals:
            v01=Roman_Numerals[a]
            print(a,'Roman Numeral is',v01)
        else:
            print(a,'Would you like to add to dictionary?')
            ans=input('\nY/N?->')
            if ans== 'Y':
                avalue=input('Enter value for key:')
                Roman_Numerals[a]=avalue
            print('-----------')
                   
        a=int(input('Enter a number:'))
        
    print("program done")
main()
