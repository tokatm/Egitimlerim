
# x^e icin oncelikle e binary bir sayiya donusturulur.



x=4
e=[0,0,1,1]


y = 1
for i in e:
    y = y * y
    if i == 1:
        y = y*x
print (y)
