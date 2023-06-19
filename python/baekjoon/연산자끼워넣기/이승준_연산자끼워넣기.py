# 핵심: permutation 구현 + 음수에 대한 나눗셈 계산
# 시간: 1시간
import sys
sys.stdin = open('number1.txt', 'r')

N = int(input())
numbers = list(map(int, input().split()))
operations = list(map(int, input().split()))

def perm(mat, k):
    result = []
    n = len(mat)
    if k == 1:
        for i in range(n):
            result.append([mat[i]])
    elif k > 1:
        for i in range(n): # 0,1,2,3,4,5 // k = 2
            ans = [mat[i] for i in range(n)] # [1,2,3,4,5,6]
            ans.remove(mat[i])
            for j in perm(ans, k-1):
                result.append([mat[i]] + j)
    return result

# step1. op_list 만들어주
op_list = []
for index, op in enumerate(operations):
    op_list.extend([index] * op)

# step2. permutation을 이용해서 operation들의 순서를 만들어주기
op_len = len(op_list)
operation_list = perm(op_list,op_len)

# step3. number와 operation을 순서대로 넣어줘서 연산 진행하기
answer = []
for operation in operation_list:
    # 1 3 0 0 2
    # if operation == [1,3,0,0,2]:
    #     print(operation)
    tmp_num = numbers[0]
    for index, real_op in enumerate(operation):
        if real_op == 0:
            tmp_num = tmp_num + numbers[index+1]
        elif real_op == 1:
            tmp_num = tmp_num - numbers[index+1]
        elif real_op == 2:
            tmp_num = tmp_num * numbers[index+1]
        elif real_op == 3:
            # tmp_num < 0 인 경우에 -1 // 3 = -1 이 나오므로 1//3 이후 -를 붙여주는 형태로 변환
            if tmp_num < 0:
                tmp_num = -((-tmp_num) // numbers[index+1])
            else:
                tmp_num = tmp_num // numbers[index + 1]
    answer.append(tmp_num)

print(max(answer), min(answer))
