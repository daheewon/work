import sys
# 최고값을 구하는 함수작성 : my_max()
def my_max(number):
    max = sys.float_info.min
    for value in number:
        if max < value :
            max = value
         
    return max

number =[ ] 
while True:
    n = int(input('숫자를 입력하세요:'))
    if n ==0:
        break
    number.append(n)
print("최대값 : {0} ".format(my_max(number)))
