def partition(numbers,start,end):
    pivot=numbers[end] 
    i = start       
    for j in range(start , end): 
        if   numbers[j] <= pivot: 
            numbers[i],numbers[j] = numbers[j],numbers[i] 
            i = i+1
    numbers[i],numbers[end] = numbers[end],numbers[i] 
    return ( i ) 
    
def quick_sort(numbers, start, end):
    while start < end:
        pi = partition(numbers, start, end)
        if(pi - 1 - start<end - pi - 1):
            quick_sort(numbers, start, pi - 1)
            start,end = pi+1, end
        else:
            quick_sort(numbers, pi+1, end)
            start,end = start, pi-1
    