name = "박영준"
print(name)

#? 문자열 사이에 문자열 추가(join)
print(",".join(name))

#! f포맷, 표현식
print(f"{name}입니다.")

#  문자열 안에서 찾고자하는 문자열의 위치 반환
print(name.find('이'))
# print(name.index('김'))

#  문자열 안에서 찾고자하는 문자열의 개수 반환
print(name.count('김'))

# 문자열 길이
print(name.__len__())
print(len(name))

print("  이름  ".strip())
print("  이름  ".rstrip())
print("  이름  ".lstrip())

# 문자열 특정 부분 변경
print("010-1234/3233".replace("-", " ").replace("/", " "))

# 토큰으로 문자열 리스트화 하기
print("박0준,박1준,박2준".split(","))

address = "부산광역시 동래구 사직동"
addressList = address.split(" ")
address1 = addressList[0]
address2 = addressList[1]
address3 = addressList[2]

# 인덱싱, 슬라이싱
print(address[0])
print(address[2:3])
print(address[:3])
print(address[4:])
print(address[-3:-1])
print(address[4:-3])
print(address[:address.find("시 ") + 1])
print(address[address.find('동') : address.find("구 ") + 1])

print(f"주소1: {address1}, 주소2: {address2}, 주소3: {address3}")
print(
f"""주소1: {address1} 
주소2: {address2}
주소3: {address3}""")





