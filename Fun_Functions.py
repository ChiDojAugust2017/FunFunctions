def odd_Evens():
    for items in range(1,2001,1):
        if items % 2 == 0:
            print items,  "Number is even!"
        else:
            print items, "Number is Odd!"
odd_Evens()

def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr

numbers_array = [3, 6, 8, 10, 67]

print multiply(numbers_array, 5)

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x