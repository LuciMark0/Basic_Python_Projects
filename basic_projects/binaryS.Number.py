x = [*range(2000)]

while True:
    try:
        y = int(input("Enter a number: "))
    except Exception as ex:
        print("\nEnter a Number!\n")
    else:
        break

# throw the usless part and keep going on the useful part
first,last,mid = 0,len(x)-1,None
while mid != first and mid != last:
    mid = (first+last)//2
    print(x[mid])
    if x[mid] == y:
        print("Your number is exist!")
        exit()
    elif x[mid] > y :
        last = mid-1
    else:
        first = mid+1

print("Your number is NOT exist!")