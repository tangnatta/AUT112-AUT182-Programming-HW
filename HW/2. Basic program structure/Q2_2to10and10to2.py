#แปลงฐาน 10 เป็นฐาน 2 และฐาน 2 เป็นฐาน 10

#โปรแกรมแปลงเลขฐาน 10 เป็นเลขฐาน 2
#ไม่สามารถทำเลขฐาน 10 ที่ติดลบได้
from typing import Counter

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
        print(timecounter)
        decimal = decimal+(int(num[(timecounter-1)]))*(2**(len(num)-timecounter))
        print((2**(timecounter-1)))
        print(int(num[(timecounter-1)]))
        print("d"+str(decimal))
        timecounter = timecounter-1
    return(decimal)

#1 หมายถึง ให้แปลงเลขฐาน 10 เป็นฐาน 2 และ หากเป็น 2 ให้แปลงเลขฐาน 2 เป็นฐาน 10
num1or2=int(input("1=10to2,2=2to10: "))
print(num1or2)
num=str(input("กรุณาใส่เลขที่ต้องการจะแปลง: "))
print(num)
if num1or2 == 1:
    result = num10to2(num)
if num1or2 == 2:
    result = num2to10(num)
print(result)