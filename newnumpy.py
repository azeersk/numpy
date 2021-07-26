from numpy import*
# single dimensional array
ar = array([10,20,30,40,50])
print(ar)

# multi dimensional array
m = array([[1,2,3,4,5,6,7], [10,20,30,40,50,60]])
print(m)

# five into five zeros
i = zeros((5,5))
a = ones((2,2))
print(a)
print(i)

# initializing numpy array with a range
r = full((4,4),25)
print(r)

# initializing numpy array with a range
range_of = arange(10,50,5)
print(range_of)

# initializing numpy array with random numbers
random_of = random.randint(1,100,5)
print(random_of)

# checking the shape of numpy arrays
s = array ([[10,20,30,40,50],[12,13,14,15,16],[23,24,25,26,27,]])
print(s.shape)

# changing shape of the array
s.shape = (5,3)
print(s.shape)
print(s)

# vertically for
li_1 = array([10,20,30,40,50])
li_2 = array([60,70,80,90,55])
v = vstack((li_1,li_2))
print(v)

# horizontally for
li_1 = array([10,20,30,40,50])
li_2 = array([60,70,80,90,55])
h = hstack((li_1,li_2))
print(h)

# for column stack
li_12 = array([10,20,30,40,50])
li_22 = array([60,70,80,90,55])
c = column_stack((li_12,li_22))
print(c)

# set in intersection
li_13 = array([10,20,30,40,50])
li_23 = array([60,70,80,20,50])
inters = intersect1d(li_13,li_23)
print(inters)

# set in difference
li_14 = array([10,20,30,40,50])
li_24= array([60,90,80,10,50])
dif = setdiff1d(li_14,li_24)
print(dif)

# addition of arrays
li_15 = array([10,20,30,40,50])
li_25 = array([60,70,80,90,55])
addi = sum([li_15,li_25])
print(addi)
sum_of_x = sum([li_15,li_25],axis = 0)
print(sum_of_x)

# basic addition & multiplication with arrays
li_16 = array([10,20,30,40,50])
li_26 = array([60,70,80,90,55])
ba = li_16 + 3
mal = li_26 * 2
print(ba)
print(mal)

# math functions
li_17 = array([10,20,30,40,50])
li_27 = array([60,70,80,90,55])
mean_of = mean(li_27)
median_of = median(li_17)
print(median_of)
print(mean_of)
print(std(li_27))
print("-----------------------------------------")
# save and load in numpy
li_19 = array([10,20,30,40,50])
sa_ve = save('my_numpy',li_19)
lo_ad = load('my_numpy.npy')
print(sa_ve)
print(lo_ad)