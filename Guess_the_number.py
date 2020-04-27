start = 1
end = 1000
mid = (int) ((start + end) / 2)
print("think of num from 1 to 1000")
print(mid)
while (True):

    if(start == end):
        print(" you thought of ", end)
        break
    ans = input(' is your num greater than ' + str(mid) + " : ")


    if (ans =="y"):
        start = mid+1
    else:
        end = mid
    mid = (int) ((start + end) / 2)
