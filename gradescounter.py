def count_fails(x):
    fails = 0
    for i in x:
        if i < 50:
            fails += 1
    return fails



grades_list = [90,70,60,50,40,34,98,22,34]
print(count_fails(grades_list))
