# chapter 1.2.2
#10진수를 16진수로 바꾸는 함수

def dec2hex(target):
    remainder = [] # 나머지를 넣을 리스트

    # 나눗셈의 몫이 0이 될 때 까지
    while target != 0:
        remainder.append(target % 16) # 나머지
        target = target // 16 # 몫

        #나머지 10~ 15를 A ~ F로 변환한다.
        for i in range(len(remainder)) :
            if remainder[i] == 10: remainder[i] = 'A'
            elif remainder[i] == 11: remainder[i] = 'B'
            elif remainder[i] == 12: remainder[i] = 'C'
            elif remainder[i] == 13: remainder[i] = 'D'
            elif remainder[i] == 14: remainder[i] = 'E'
            elif remainder[i] == 15: remainder[i] = 'F'

    # 리스트에 있는 요소를 역순으로 반환한다
    remainder.reverse()
    return remainder

print(dec2hex(31))