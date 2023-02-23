x = input()
print(x)
x = list(x)
x_origin = x[:]
y = list()

for i in range(len(x)):
	y.append(x.pop())
if x_origin == y:
	print('입력하신 단어는 회문(Palindrome)입니다.')
 
 
# chatGPT

def reverse_string(s):
    # 문자열을 리스트로 변환 후 뒤집기
    reversed_list = list(s)[::-1]
    # 리스트를 문자열로 변환하여 반환
    return ''.join(reversed_list)

# 회문 여부를 판단하는 함수
def is_palindrome(s):
    reversed_s = reverse_string(s)
    if s == reversed_s:
        return True
    else:
        return False

# 회문 여부를 판단하는 코드
word = input("단어를 입력하세요: ")
if is_palindrome(word):
    print("입력한 단어는 회문입니다.")
else:
    print("입력한 단어는 회문이 아닙니다.")