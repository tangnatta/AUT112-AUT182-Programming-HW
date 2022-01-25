#โปรแกรมแปลงเลขฐาน 10 เป็นเลขฐาน 2
#ไม่สามารถทำเลขฐาน 10 ที่ติดลบได้
decimal = int(input("กรุณาใส่เลขฐาน 10: "))
bit_2 = ""

#Original
def num10to2original(bit_2,decimal):
    remain = decimal
    print("---- LOG ----")
    while remain > 0:
        bit_2 = str(remain%2)+str(bit_2)
        print(bit_2)
        remain = remain//2
        print(remain)
        if remain <= 0:
            print("---- END LOG ----")
            print("RESULT:"+str(bit_2))

#sync with flowchart
def num10to2(bit_2,decimal):
    while decimal > 0:
        bit_2 = str(decimal%2)+str(bit_2)
        print("ฐาน 2: "+str(bit_2))
        decimal = decimal//2
        print("ฐาน 10 ที่เหลือ: "+str(decimal))
    print("RESULT:"+str(bit_2))

num10to2(bit_2,decimal)