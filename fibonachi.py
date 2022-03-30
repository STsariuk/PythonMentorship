'''def GetFibonacciList(n, L):
    count = len(L)
    if len(L)<2:
        return []
    num1 = L[count-2]
    num2 = L[count-1]
    if (num1+num2) < n:
        L = L + [num1+num2]
        return GetFibonacciList(n, L)
    else:
        return L
LL = GetFibonacciList(7, [0, 1])
print("LL = ", LL)'''

def fibonachi(num):
    n1 = 0
    n2 = 1
    count = 0
    while count < num:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        # print(nth)
    return nth
fibo_six = fibonachi(6)
print(fibo_six)