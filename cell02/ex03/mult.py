x = int(input('Enter the first number:'))
y = int(input('Enter the second number:'))
print(x,'X', y , ' =',x * y)

if x * y < 0:
    print("This result is negative.")
elif x * y > 0: 
    print("This result is positive.")
else: 
    print("This result is both positive and negative.")
