def add_two_numbers(a,b):
    sum=a+b
    return sum
x=add_two_numbers(5,4)
a=5 
b=4
print("The sum of {} and {} is {}".format(a,b,x))


def reverse_list(A,size):
   if(size==1):
     return arr
   elif(size==2):
        arr[0],arr[1]=arr[1],arr[0]
        return arr
   else:
     i=0
     while(i<size/2):
        arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
        if((i!=i+1 and size-i-1!=size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
         arr[i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
        i+=2
   return arr
arr=[1,2,3,4,5]
size=5
print("Reverse list: ",reverse_list(arr,size))
    


def even_and_odd(a):
    if a%2==0:
      print("Even Numbers " ,int(a/2))
      print("Odd Numbers " ,int((a/2)+1))
    else :
        print("Even Numbers" ,int((a/2)+1))
        print("Odd Numbers " ,int((a/2)+1))
even_and_odd(1)
