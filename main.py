## 함수선언부
def add_func(n1, n2) :
    return n1 + n2

def sub_func(n1, n2) :
    return n1 - n2

def mul_func(n1, n2) :
    return n1 * n2

def pow_func(n1, n2) :
    return n1 ** n2



## 전역변수부
num1, num2 = 100, 200
result = 0


## 메인코드부
result = add_func(num1, num2)
print(num1, "+", num2, "=", result)

result = sub_func(num1, num2)
print(num1, "-", num2, "=", result)

result = mul_func(num1, num2)
print(num1, "*", num2, "=", result)

result = pow_func(num1, num2)
print(num1, "**", num2, "=", result)

