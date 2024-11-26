#Donavan Bryant property tax program calculator 2
def getinput(msg):
    xin = float(input(msg))
    return xin

def main():
    print('\n'*3)
    AssessmentLevel = .10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45
    PropertyValue = getinput('Enter value of property:')
    LocalTaxRate = getinput('Enter local tax rate:')
    StateEqualizer = getinput('Enter state equalizer rate:')
    print('\n'*3)
    AssessedValue= PropertyValue * AssessmentLevel
    EqualizedValue = AssessedValue * StateEqualizer
    PropertyTaxBefore = EqualizedValue * LocalTaxRate
    TotalPropertyTax = PropertyTaxBefore - HomeOwnerEx - SeniorCEX
    print('\n'*3)
    print('Property tax due: ',TotalPropertyTax)
    print('\n'*3)
    return
main()
