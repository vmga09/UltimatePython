# Set significa grupo o conjunto

primer = {1,2,2,3,3,4,56,7,8}
print(primer)

segundo = [7,8,9,10]
segundo = set(segundo)

print(primer|segundo)
print(primer & segundo)
print(primer - segundo)
print(primer ^ segundo)