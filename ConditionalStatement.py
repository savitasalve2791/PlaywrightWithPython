print("=========================================")
#WAP to compare two strings
expectedvalue=input("please enter your expected value-->")
actualvalue=input("please enter your actual value-->")
if expectedvalue==actualvalue:
    print("the expected value is equal to actual value")
else:
    print("the expected value is different from actual value")
#WAP cross browser testings
browserName=input("please enter your browser-->")
browserName=browserName.lower().strip()
if browserName=="firefox":
    print("the browser is firefox")
elif browserName=="chrome" :
    print("the browser is chrome")
elif browserName=="safari" :
    print("the browser is safari")
elif browserName=="edge" :
    print("the browser is edge")
else:
    print("Playwright is not supporting this browser and browser name is-->"+browserName)
print("====================For Loop Statement============================")
#range() values between the range range(start index , end index) , end index is excluded
print(list(range(1,10)))
#while loop print
i=1
while i<=10:
    print(i)
    i=i+1
i=10
while i>=1:
    print(i)
    i=i-1
#for loop
print("=========For loop incremented=============")
for i in range(1,10,1):
    print(i)
print("=========For loop decremented=============")
for i in range(10,0,-1):
    print(i)
print("=========For loop skip=============")
for i in range(1,10,2):
    print(i)
print("=========For loop break=============")
for i in range(1,10,1):
    if i==6:
        break
    print(i)
print("=========For loop continue=============")
for i in range(1,10,1):
    if i==5:
        continue
    print(i)





