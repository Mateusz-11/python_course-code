def calculate_common_divisor(num1, num2, start=2):
    set1 = set()
    set2 = set()
    for i in range(start, num1+1):
        if num1 % i == 0:
            set1.add(i)
    for j in range(start, num2+1):
        if num2 % j == 0:
            set2.add(j)
    return set2 & set1


print("Common dividers:", calculate_common_divisor(3,6))

print('- - -' * 5)
print("Common dividers:", calculate_common_divisor(3,6, 4))

print('- - -' * 5)
print("Common dividers:", calculate_common_divisor(16,8))