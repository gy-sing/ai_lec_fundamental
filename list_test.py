subject = ['국어', '영어', '수학', '사회', '과학']
scores = [100, 90, 100, 40, 45]

print(subject)
print(scores)

print(type(subject))
print(type(scores))

print(len(subject))
print(len(scores))
# subject[2] = "체육"
# print(subject)

print(subject)
print(subject[1:])
print(subject[1:3])
print(subject[:3])
print(subject[-1])

#리스트에 데이터 추가
subject.append("한국사")
print(subject)
subject.append(112)
print(subject)
print(" ")

#리스트에서 데이터 제거
#인덱스로 제거 del명령어 or pop()함수

print(subject)
del subject[-1]
print(subject)

print(subject.pop())
print(subject)


#데이터를 직접 제거 remove()함수
subject.remove('사회')
print(subject)

university = "전북대학교"

print(university[0])
print(university[1])





