# num1 = int(input("숫자1: "))
# num2 = int(input("숫자2: "))

#  10, 20
#  10 20
num1AndNum2 = list(map(int, input("숫자1, 숫자2 : ").replace(",","").split(" ")))
print(num1AndNum2)

n1AndN2Input = input("숫자1, 숫자2 :").replace(",","").split(" ")
n1AndN2 = list(map(int, n1AndN2Input))
print(n1AndN2)

num1, num2 = n1AndN2
print(num1)
print(num2)


# nums = ['1', '2', '3', '4']
# nums2 = list(map(int, nums))
# print(nums2)

# def parseInt(strNum):
#   return int(strNum)
# nums3 = list(map(parseInt, nums))

# print(nums3)
# nums4 = list(map(lambda strNum: int(strNum), nums))