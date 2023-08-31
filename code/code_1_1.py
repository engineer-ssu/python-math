# chapter 1.2.1
# 10진수 값을 2진수로 변환하는 함수를 만들어보자
# bin() 함수와 동일한 로직을 실행한다.
# 표시하는 방법은 bin() 함수와 다르지만, 숫자를 나열하는 방법은 같다.


def dec2bin(target):
    otherlist = []

    while target != 0:
        otherlist.append(target % 2)
        target = target // 2

    # 리스트에 있는 요를 역순으로 바꿔서 반환한다.
    otherlist.reverse()
    return otherlist

print(bin(26))
#0b11010

print(dec2bin(26))
