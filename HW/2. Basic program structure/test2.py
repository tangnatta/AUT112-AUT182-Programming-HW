def num10to2(num):
    num = int(num)
    bit_2 = ""
    while num > 0:
        bit_2 = str(num%2)+str(bit_2)
        print("ฐาน 2: "+str(bit_2))
        num = num//2
        print("ฐาน 10 ที่เหลือ: "+str(num))
    print("RESULT:"+str(bit_2))
    return(bit_2)

def num2to10(num):
    decimal = 0
    timecounter = len(num)
    for i in range(len(num)):
        decimal = decimal+(int(num[(timecounter-1)]))*(2**(len(num)-timecounter))
        timecounter = timecounter-1
    return(decimal)

truecounter = 0
time = 0
for i in range(10):
    print("2: "+str(num10to2(time)))
    print("10: "+str(num2to10(num10to2(time))))
    if num2to10(num10to2(time)) == time:
        print("true")
        truecounter= truecounter+1
    time=time+1
print(truecounter)