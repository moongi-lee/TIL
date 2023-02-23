# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다.
#
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다.
#
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
#
# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤 append로 각 줄을 추가하면 됩니다(list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).
# initialize = list(map(int, input().split()))
initialize = list(map(int, input().split()))
colom = initialize[0]
matrix = []
for i in range(colom):
    matrix.append(list(input()))

for i in range(colom):
    for j in range(colom):
        if matrix[i][j] != '*':
            matrix[i][j] = 0


for i in range(colom):
    for j in range(colom):
        if matrix[i][j] != '*':
            for k in range(i - 1, i + 2):
                for p in range(j - 1, j + 2):
                    if k!=i or p!=j:
                        if not(k < 0 or k == colom or p < 0 or p == colom):
                            if matrix[k][p] == '*':
                                matrix[i][j] = matrix[i][j] + 1
for i in range(colom):
    for j in range(colom):
        print(matrix[i][j], sep='', end='')
    print()