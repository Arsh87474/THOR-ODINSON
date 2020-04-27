print("I am the PALINDROME checker")
p = input('Enter a any word or number and I will tell if it is a palindrome:\n')

mid = int(len(p) / 2)
for x in range(mid):
    if p[x] != p[- (x + 1)]:
        print("This is not a palindrome.")
        exit(0)

print("It is a palindrome")
