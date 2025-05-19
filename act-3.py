import array as arr
x=arr.array('i', [1,5,7,9,1,1,4,5,5,5,7,7])
print("Array:"+str(x))
print("No.of occurence(Num:5)"+str(x.count(5)))

x.reverse()
print("Reverse array:",str(x))