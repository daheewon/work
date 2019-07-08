# 1. my_join함수 구현 -> str1과 str2 문자열을 결합하여 리턴하는 함수 
def my_join( str1, str2 ):
    return str1+str2
str1 = input ('문장을 입력해 주세요:')
str2 = input ('문장을 입력해 주세요:')
print (my_join( str1 , str2 ))


import sys
# 최고값을 구하는 함수작성 : my_max()
def my_max(number):
    max = sys.float_info.min
    for i in number:
        if max < i :
            max = i
         
    return max

number =[ ] 
while True:
    n = int(input('숫자를 입력하세요:'))
    if n ==0:
        break
    number.append(n)
print("최대값 : {0} ".format(my_max(number)))
