nums = []
text = []
mix = []

usrstr = input("Enter any value (numbers, text or a mix). Enter when q you are done entering values: ")
while "q" not in usrstr:

    if usrstr.isalpha():
        text.append(usrstr)
    elif usrstr.isdigit():
        nums.append(usrstr)
    else:
        mix.append(usrstr)
        
    usrstr = input("Enter any value (numbers, text or a mix). Enter when q you are done entering values: ")

print("You entered the following numbers")
total = 0
for num in nums:
    print(num)
    total += int(num)
print(f"The sum of those numbers is: {total}")

print("You entered the following words")
for word in text:
    print(word)



print("You entered the following values which contain a mix of numbers, letters, and characters: ")
for m in mix:
    print(m)
