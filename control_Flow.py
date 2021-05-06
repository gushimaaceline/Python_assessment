a={6,7,8,9,10}
b={5,6,7,8,9}
a.add(4)
print(a)
b.add(3)
print(b)
lst=[11,100,99,1000,999,99]
lst[0]=-1
print(lst)
print(lst[0])
print(lst[5])
count=0
for items in lst:
    if items==99:
        count+=1
print (count)
print(sum(lst))
print(min(lst))
years=range(2020,2070)
for year in years:
    if year%4 == 0:
        print(year)

numbers=range(1000,2000)
for num in numbers:
    if num%7==0 and num%5!=0:
        print(num)

nums=range(1,11)
for n in nums:
    print(n)
odd=range(30,50)
for num in odd:
    if num%2!=0:
        print(num)

x=[]
items=range(100,200)
for i in items:
    if items%7==0:
        x.append(i)
print(x)

myNumbers=range(1,50)
for item in myNumbers:
    if item%3==0 and item%5==0:
        print("purpleWhite")
    if item%5==0:
        print("White")
    if item%3==0:
        print("purple")
