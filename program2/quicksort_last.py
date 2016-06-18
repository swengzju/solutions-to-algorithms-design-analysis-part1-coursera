count = 0
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   global count
   
   pivotvalue = alist[last]
   alist[last] = alist[first]
   alist[first] = pivotvalue

   i = first + 1
   for j in range(first + 1, last + 1):
           count = count + 1
           if alist[j] < pivotvalue:
                   temp = alist[i]
                   alist[i] = alist[j]
                   alist[j] = temp
                   i = i + 1
   temp = alist[first]
   alist[first] = alist[i-1]
   alist[i-1] = temp
   return i-1

with open("/Users/wengsheng_/Desktop/Algorithms part 1/Program two/QuickSort.txt") as f:
        data = f.readlines()
alist = map(int, data)
quickSort(alist)
print(count)
