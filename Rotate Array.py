#Rotate array

def rotate(array,k):
    n = len(array)
    k = k%n
    return array[n-k:]+array[:n-k]

array =[1,2,3,4,5,6,7]
k = 3
print(rotate(array,k))