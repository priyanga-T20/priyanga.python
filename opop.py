
#1
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int (input("enter the third number:"))
if a>=b and a>=c:
    print("Largest number=",a)
elif b>=c and b>=a:
    print("Largest number=",b)
else:
     print("Largest number=",c)
#2
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int (input("enter the third number:"))
if a<=b and a<=c:
    print("smallest number=",a)
elif b<=c and b<=a:
    print("smallest number=",b)
else:
     print("smallest number=",c)
#3
num=int(input("enter the number:")) 
if num>0:
        print("Positive",num)
elif num<0:
    print("Negative",num) 
else:
    print("It is Zero")
#4
late=int(input("enter the no of days books were returned late:"))
if late <6 and late>0:
    print("40 paise per day")
elif late >5 and late<11:
    print("65 paise per day")
elif late>10:
    print("80 paise per day")
else:
    print("No  Fine Fee")

#5
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter opertors(+,-,*,/):"))
if op=='+':
    print("sum=",a+b)
elif op=='-':
    print("difference:",a-b)
elif op=='*':
    print("product:",a*b)
elif op=='/':
    print("quotient",a/b)
else:
        print("invalid operator")
#6
n=int(input("enter a number:"))
if  n%5==0 and n%3==0 and n%7==0:
    print("multiple by 5,3 and 7")
else:
        print(" not multiple by 5,3 and 7")
#7
w=int(input("enter the weight in gm:"))
t=int(input("choice: \no----for ordinary delivery\n E ----for express deivery\n enter your choice:"))
if w<=100 and w>0:
 if t=='o' or t=='O':
     print(" Delivery charge is rs,80")
elif t=='e' or t=='E':
   print(" Delivery charge is rs,100")
else:
 print("invalid choice")
elif w>100 and w<501 :
     if t=='o' or t=='O':
        print(" Delivery charge is rs,150")
 elif t=='e' or t=='E':
        print(" Delivery charge is rs,200")
 else:
    print("invalid choice")
 elif w>500 and w<1001 :
    if t=='o' or t=='O':
        print(" Delivery charge is rs,210")
 elif t=='e' or t=='E':
        print(" Delivery charge is rs,250")
 else:
    print("invalid choice")
 elif w>1000 :
    if t=='o' or t=='O':
        print(" Delivery charge is rs,250")
 elif t=='e' or t=='E':
        print(" Delivery charge is rs,300")
 else:
    print("invalid choice")
 else:
    print("enter a valid amount")
#8
price=int(input("enter"))
print(price)
if price<=50000:
    discount=0
elif price<=100000:
     discount=price * 10/100
elif price<=150000:
        discount=price * 15/100
else:
        discount=price * 20/100
total_price= price -discount
print("price of laptop:",price)
print("discount:",discount)
print("total pice:",total_price)




    
