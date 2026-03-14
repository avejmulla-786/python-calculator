arr=[10,20,30,40]

#traversal
print("arr:",arr)

#inserstion at end
arr.append(50)
print("after insertion:",arr)

#deletation
arr.remove(30)
print("after deletion:",arr)

#searching
x=40
if x in arr:
    print("F{x}found in index",arr.index(x))
else:
    print("not found")
