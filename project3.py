

#taking input from user

price=int(input("Enter price of item: "))
#taking input from user  
discount_perc=float(input("Enter discount %:"))
#calculating discount
discount_amt=(price/100)*discount_perc
#calculating final amount
final_price=price-discount_amt
#printing output
print("final price: {}".format(final_price))


