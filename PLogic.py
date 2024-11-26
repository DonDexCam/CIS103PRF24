#Donavan Bryant using Logic

pounds=float(input('enter pounds'))
price_per_pound=.99
gross_sales=pounds*price_per_pound
print=('gross is', gross_sales)
discount=0
if (pounds>=10) and (pounds<99.99):
    discount=.1
    print('discount is', discount)
else:
    if(pounds>=100) and (pounds<999.99):
        discount=.2
        print('discount is', discount)
    else:
        if(pounds>=1000) and (pounds<9999.99):
            discount=.3
            print('discount is', discount)
        else:
            if(pounds>=10000):
                discount=.4
                print('discount is', discount)
discount_amt=gross_sales*discount
final_amt=gross_sales-discount_amt
print('discount_amt is', discount_amt)
print('final_amt is', final_amt)
