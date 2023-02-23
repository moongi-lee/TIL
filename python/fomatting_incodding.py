#소문자
x = int(input())
print('%x'% x)

#대문자
x = int(input())
print('%X'% x)

#16진수로 저장
x = int(input(), 16)
print('%o'% x)

#문자를 ~ 유니코드로 저장
n = ord(input())
print(n)

#숫자를 ~ 유니코드로 변환
x = int(input())
print(chr(x))

#유니코드 덧셈으로 문자 전환
x = ord(input())
print(chr(x+1))

#도대체 무슨 원리야?