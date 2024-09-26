def sumfunc (n) :
    total = 0
    for i in range(1, n+1) :
        total += i
    return total
try:
    num = int(input("임의의 정수를 입력하세요: "))
    
    if num <= 1:
        print("잘못 입력하였습니다. 1보다 큰 정수를 입력하세요.")
    else:   
        result = sumfunc(num)
        print(f"1부터 {num}까지의 합은 {result}입니다.")
    
except ValueError:
    print("유효한 정수를 입력하세요.")