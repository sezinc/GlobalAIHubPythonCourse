nums2=list(range(10))
print("List=",nums2)

a=int(len(nums2)/2)
b=int(len(nums2))

x=slice(0,a)
y=slice(a,b)
print("Swap List= " ,nums2[y]+nums2[x])