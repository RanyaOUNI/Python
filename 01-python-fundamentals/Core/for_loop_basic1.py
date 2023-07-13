
#---------- INTEGERS FROM 0 TO 150 -----------

for i in range(0,151):
    print(i)

print("************")

#---------- MULTIPLES OF FIVE ----------------

for i in range(5,5001):
    if (i%5==0):
        print(i)

print("************")

#----------- COUNTING THE DOJO WAY -----------

for i in range(1,101):
    if (i%10==0):
        print("Coding Dojo")
    elif (i%5==0):
        print("Coding")
    else:
        print(i)

print("************")

#------------ Whoa. That sucker's Huge ---------
sum=0
for i in range(0,500001):
    if (i%2!=0):
        sum+=i
print(sum)

print("************")


#------------ Countdown by Fours ---------------

for i in range(2018,0,-4):
    print(i)

print("************")

#------------ Flexible Counter -----------------
def Flexible(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if (i%mult==0):
            print(i)
Flexible(2,9,3)
