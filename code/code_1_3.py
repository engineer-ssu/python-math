# chapter 1.2.3
#int()함수와 같이 다른 기수법에서 10진수로 변환하는 작업을 프로그램으로 만들어 본다.
# 첫번째 인수에는 변환하기 이전의 값을 문자열의 형태로 넣고 두 번째 인수에는 기수를 넣는다

def any2dec(target, m):
    n = len(target)-1 # 지수 최댓값은 target자릿수에서 항상 1을 뺀 값이다. 그보다 클 수 없다.
    sum = 0 # 10진수로 변환한 값

    #문자 수만큼 반복
    for i in range(len(target)):
        if target[i] == 'A': num = 10
        elif target[i] == 'B': num = 11
        elif target[i] == 'C': num = 12
        elif target[i] == 'D': num = 13
        elif target[i] == 'E': num = 14
        elif target[i] == 'F': num = 15
        else: num = int(target[i])

        sum+= (m ** n) * num # "m의 n승 x 각 행의 값"의 한계를 구한다
        n -= 1              # 무게를 한 개 줄인다

    return sum

print(any2dec('11010', 2))