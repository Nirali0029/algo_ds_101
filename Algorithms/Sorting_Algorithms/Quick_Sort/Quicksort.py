def partition(a,low,high):
    i=(low-1)
    pivot=a[high]
    for j in range(low,high):
        if a[j]<pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return (i+1)

def quick_sort(a,low,high):
    if len(a)==1:
        return a
    if low<high:
        k=partition(a,low,high)
        quick_sort(a,low,k-1)
        quick_sort(a,k+1,high)


a=[10,9,6,3,4,1,2]
quick_sort(a,0,(len(a)-1))

print("After applying quick sort")
for i in range(len(a)):
    print(a[i],end=" ")
