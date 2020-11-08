# exponential growth program that proves MU's puzzle is impossible
# declares growth variable which is the power that two is risen by
growth = 0
expoGrowth = 0
growing = True
# while loop raises two by an ever increasing power
while growing:
    expoGrowth = 2 ** growth
    growth += 1
    print(growth)
    # checks if 2 ^ growth modulus 3 leaves no remainder, thus dividable by 3
    if expoGrowth % 3 == 0:
        growing = False
    else:
        growing = True
