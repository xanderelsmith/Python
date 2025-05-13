arr=[45,32,1,23,456,44,33.3,32]

def findLargest(arr,n):
    largest=0
    for number in range(0,n):
        if largest<arr[number]:
            largest=arr[number]
    return largest

arrayLength=len(arr)
largest=findLargest(arr,arrayLength)
print(largest)


# input string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
# apending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))