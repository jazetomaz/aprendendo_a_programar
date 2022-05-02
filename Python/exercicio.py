largest = None
smallest = None
num = 0

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        numint = int(num)
    except:
        print('Invalid input')
        continue

    if smallest is None:
        smallest = numint
    elif numint < smallest:
        smallest = numint

    if largest is None:
        largest = numint
    elif numint > largest:
        largest = numint


print("Maximum is", largest)
print("Minimum is", smallest)
