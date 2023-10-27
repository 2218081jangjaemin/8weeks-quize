def check_jumin(jumin):
    if len(jumin) != 13:
        return False

    factors = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    sum = 0

    for i in range(12):
        sum += int(jumin[i]) * factors[i]

    remainder = sum % 11
    result = (11 - remainder) % 10

    return result == int(jumin[12])

jumin = input("주민등록번호를 입력하세요: ")
if check_jumin(jumin):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
