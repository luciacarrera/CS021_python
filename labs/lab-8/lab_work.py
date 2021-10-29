## PART ONE
print("############## PART ONE ############## ")

# 1
years = [2016,1620,1984,1776,1860,1492]
print(type(years))

print(years)

print(years[1])

print(years[2:5])

print("min:",min(years),"max:", max(years),"\n\n")

for year in years:
    print(year)


n = len(years)
for i in range(0,n):
    print("Yr"+str(i),str(years[i]),sep=": ")


# 2
years2 = (2016,1620,1984,1776,1860,1492) # parenthesis

print("\n",type(years2))

# 3
years[4]= 1984
print(years)


# 4
try:
    years2[4]= 1865
except:
    print("Error: 'tuple' object does not support item assignment")

    
# 5
years.remove(1984) # no because there are two values and only removes first value
print(years)
try:
    years2.remove(1984)
except:
    print("Error: 'tuple' object has no attribute 'remove'")


# 6
years.sort()
print("\n Sorting: ",years)
years.reverse()
print(years)

try:
    years2.sort()
except:
    print("'tuple' object has no attribute 'sort'")
try:
    years2.reverse()
except:
        print("'tuple' object has no attribute 'reverse'")


## PART TWO
print("\n\n############## PART TWO ############## ")

# 1
dorms = []
print(len(dorms))

# 2
dorms.append("Converse")
print(dorms)


# 3
dorms.insert(0,"Mason")
print(dorms)
print(dorms.index("Converse"))

# 4
dorms.append(['UHeights','Redstone','Trinity']) ## extra []
print(dorms[2])
print(type(dorms[2])) # type correct?

dorms += ['Christie','Wright','Patterson']
print(dorms)

# 5
central = ["WE","Converse"] 
athletic = ["UHeights","Harris/Millis","MAT", "L/L"] 
redstone = ["CWP", "SMH", "WDW"] 
housing = [central, athletic, redstone]
print(type(housing))
print(type(housing[0]))
print(type(housing[0][0]))
print(housing[1][2])

## PART THREE
print("\n\n############## PART THREE ############## ")

# 1
odds = []
for i in range(51,68,2):
    odds.append(i)
print(odds)

evens = []
for i in range(0,11,2):
    evens.append(i)
print(evens)
nums = odds + evens
print(nums)

# 2
nums2 = nums

# 3
del nums[5]
print("nums: ",nums)
print("nums2: ",nums2) # 61 removed from both nums and nums2

# 4
nums = [] + nums
del nums[5]
print("nums: ",nums)
print("nums2: ",nums2) # not deleted from nums 2




