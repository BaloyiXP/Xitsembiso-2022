#ask for digits number
while True:
    try:
      num=int(input("Please enter any five digits: "))
      

      
    except ValueError:
        print("Sorry, please enter again")
    else: 
        break

print("The number entered is : ",num)

rev=0
sum=0
sum2=0
temp_sum=0
number=num

dig = list(map(int, list(str(num))))
#reverses the number entered
while(num!=0):
    rem=num%10
    rev=(rev*10)+rem
    remainder=number%10
    sum=sum+remainder
    number=number//10
    temp = rem + 1
    if(temp==10):
        temp=0
    num=num//10
    sum2 =(sum2*10)+temp
  
print("The reverse of the number is :",rev)
print("The sum of digits=",sum)
#reverse the new number
r=0
while(sum2!=0):
    
    i = sum2%10
    r=(r*10)+i
    sum2=sum2//10
print("The new number after adding one  to each",r)

