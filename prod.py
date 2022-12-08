#using input function 
product1=int(input("quality of first product:"))
product2=int(input("quality of second product:"))
product3=int(input("quality of third product:"))
#product4=int(input("quality of four product:"))
#product5=int(input("quality of five product:"))
#price1=int(input("price of product1:"))
#price2=int(input("price of product2:"))
#price3=int(input("price of product3:"))
#using the list
#l=[product1,product2,product3]
#using the for loop
#for i in l:
 #   print(i)
#using if_else statements    
if((product1<=0) or (product2<=0) or (product3<=0)):
    print("please enter a positive value")
else:
    print("product quantity with price:")
    totalamount=product1*300 +product2*500+product3*600
    entries = {product1:300,product2:400,product3:200}
    for i,p in entries.items():
        print(i,p)
    print('the amount that yu need to pay is:')    
    print(totalamount)  
