# l=[1,2,3,4,5]
# print(list(filter(lambda x:x>2,l)))
from scipy import integrate
a=integrate.quad(lambda x:(x**2+x+1),0,3)
print(len(a))
print(a[0])

