#variables
a=1
b="sohel"
c=str('JHJSHJ')
d=float(33)
A="print something"
print(a," ",b," ",c," ",d," ",A)
print(type(A)),print(type(a)),print(type(b)),print(type(c)),print(type(d))
print('python version')
#name variables
myvar="its me"
print(myvar)
#assign multiple values
a,b,c="sohel","mazz","tanveer"
x=y=z="my name is sohel"
subjects=[90,70,60]
p,q,r=subjects
print(a)
print(b)
print(c)
print(x)
print(y)
print(z)
print(p)
print(q)
print(r)
#output variables
x="i a awesome"
y=", really i am"
z=x+y
a=1235
b=1235
print(z)
print(x+y+z)
print(a+b)
print(z,a+b)
#gloabal variables
a="sohel"
def myfun():
    print("i am  "+a) 
myfun()
x="excellent"
def myfun():
    x="not good"
    print("i am  "+x)
myfun()

print("i am  "+x)
#python data types
a=112
b="hi everyone"
c=3.2
d=True
e=["maaz", "tanveer","fazal","sohel"]
f={123,125,"maaz","hey"}
g=("ask me",200,"rupees")
h={"name:sohel","age:23"}
i=({"name:sohel","age:23"})
j=5j
k= b'helloooooo'
l=range(100)
m=bytearray(125)
n=memoryview(bytes(1254786))
#resul of data types

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
#numbers
x=int(1222)
y=complex(112131212125315721231231217j)
z=float(2)
import random
print(random.randrange(17,20))
print(x)
print(y)
print(z)
#casting
#INT
A=int(1)
B=int(1.9)
C=int("1")
#FLOAT
D=float(2)
E=float(2.35)
F=float("45")
#string
G=str(122)
H=str("hgkjhjh")
I=str(3.253)
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)
print(I)
#strings
a="hello"
b='how are you'
c="""hey fazal"""
d='''how are you'''
print(a)
print(b)
print(c)
print(d)
#strings array
text="i dont know how to do it"
print(text)
text1="what you know then"
for text1 in "you":
 print(text1)
text3="fazal what are you doing"
print(len(text3))
text4=" hey what are you  dooing man"
print("hey" in text4)
text5="is that easy to handle you"
if "easy" in text5:
  print("yes, its present in it")
text6=" i dont know you , how come you now about me"
print("know" not in text6)
text7="ho the hell you are to talk me like that"
if "how" not in text7:
        print("Yes, it is not present in it")
#slicing index
m="maaz how are you going to do it yourself"
print(m[0:16])
print(m[23:])
print(m[26:44])
print(m[-8:-0])
#modifyoing strings
t=" tanveer where ,you are in the whole  night"
print(t.upper())
print(t.lower())
print(t.strip())
print(t.replace("tanveer", "fazal"))
print(t.split(","))
#String Concatenation
a="meri ek taang nakli hai"
b="aur mai hokey ka bada player tha"
c=a+b
d=a+" "+b
print(c)
print(d)
#String Format
gen="male"
a=" my gender is {}"
print(a.format(gen))
x="i am {} and i will be {} dont know {} "
p="26"
q="dont know"
r="23223"
print(x.format(p,q,r))
x="i am {2} and i will be {1} dont know {0} "
print(x.format(p,q,r))
#Boolean Values
#comparing with numbers using assignments
print(9==9)
print(9<11)
print(9>11)
#messege based true and false
a=10
b=30
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

a=30
b=10
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")
#printing directly bool
print(bool("hey"))
print(bool(1230457896j))
#most values are true like
print(bool("23325"))
print(bool((a,b,c)))
print(bool({"hey", "ho are you"}))
print(bool([12,13,14]))
print(bool({"nam,e:sohel","age:26"}))
print(bool(0))
#except this empty values
print(bool(()))
print(bool({}))
print(bool([]))
print(bool({}))
print(bool())
#using functios calling the functions
def myteam():
    return True
print(myteam())
def mylegecy():
    return False
if mylegecy():
    print("no")
else:
    print("yessss")
#python operators
print(5+5)
#python arithmetic operators
x=100
y=200
print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x**y)
print(x%y)
print(x//y)
#python assignment operators
a=10
b=10
c=10
d=10
e=10
f=10
g=10
a+=3
b-=3
c*=3
d/=3
e**=3
f%=3
g//=3

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(a)
#python assining operators
p=100
q=200
print(p==q)
print(p!=q)
print(p<=q)
print(p>=q)
print(p<q)
print(p>q)
#python logical operators(and,or,not)
#or operator
x=10
y=20
print(x<y or x>y)
print(x>y or y<x)
#and operator
print(x<y and y>x)
print(x>y and y<x)
print(x<y and y<x)
#not operators
print(not(x<y and y<x))
print(not(x<y or x>y))
#python identifier operators
x=[25]
y=[25]
z=x
print(x is z)
print(x==y)
print(x is y)
#Python Membership Operators
x=[10,20,30]
print(10 in x)
print(40 in x)
print(40 not in x)
print(20 not in x)
#List
list1=["maaz", "tanver", "fazal"]
list2=["maaz", 123, "fazal"]
list3=["maaz", True, "fazal", "maaz"]
list4=["maaz", "tanver", "fazal"]
list5=list(("saqeeb",123456789))
print(type(list1))
print(len(list1))
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list1[1])
#list methods
a=[1,2,3,"me","you","we",3,2,1]
b=[3,4,5,"me","you","we",5,4,3]
a.append("myself")
print(a)
a.append(b)
print(a)
c=a.count(3)
print(c)
b.clear
print(b)
a.clear
print(a)
b=[20]
c=[12358,258974152693,145879631]
b.extend(c)
print(b)
d=c.index(12358)
print(d)
c.insert(2, "hey")
print(c)
c.pop(2)
print(c)
c.pop(1)
print(c)
h=["my name is sohel","my age is about 26"]
print(e)

print(e)
h.reverse()
print(h)
h.append(i)
print(h)
#h.sort()
print(h)
A=["ABDUL","ZOHAN","CARRY"]
A.sort()
print(A)
#TUPLE
a=(1,2,3,"me","you","we",3,2,1)
b=(3,4,5,"me","you","we",5,4,3)
z=tuple(("go away from hjere","why its like that",123,True))
print(type(a))
print(len(b))
print(z)
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)





