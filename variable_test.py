"""
# 변수


x = 3
pi = 3.141592
university = "전북대학교"
location = "전주시"

print(pi)
print(university + location)

print(x)
x = x+1
print(x)
x += 1
print(x)

print(type("얄코"))

str_x = str(x)
print(type(str_x))
print(str_x)
float_x = float(x)
print(float_x)

month = 7
date = 20
day = "수"

print("오늘은 %s요일입니다." %day)
print("오늘은 %d월 %d일 %s요일입니다." %(month, date, day))
print("오늘은 {}월 {}일 {}요일입니다." .format(month, date, day))
print("오늘은 {m}월 {d}일 {da}입니다." .format(m=7, d=18, da="월요일"))
print(f"오늘은 {month}월 {date}일 {day}요일 입니다.")

str1 = "오늘은"
str2 = "7"
str3 = "월"
str4 = "20"
str5 = "일"
str6 = "입니다."

print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())
print(str4.isalpha())
print(str5.isalpha())
print(str6.isalpha())

print(str1.isdigit())
print(str2.isalpha())
print(str3.isalpha())
print(str4.isalpha())
print(str5.isalpha())
print(str6.isalpha())

day1 = input("요일을 입력해주세요 >>")
print(f"오늘은 {day1}")
"""

month, date, day = input("월, 일, 요일을 입력해주세요 >>").split()
print(f"오늘은 {month}월 {date}일 {day}요일입니다.")








"""
주석처리는 # or """ """
파이썬에서는  변수에 type을 생각안해도 됨. >>> 편리함
캐스팅변수 : 캐스트 연산자( str, float, int)데이터 앞에서 타입을 지정해 주는것 
"""