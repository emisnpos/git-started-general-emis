
my_list = [88, 2, 3, 28, 99, 23, 55, 11, 67, 69, 1, 107]
new_list = []

while my_list:
    max = my_list[0]  
    for x in my_list: 
        if x > max:
            max = x
    new_list.append(max)
    my_list.remove(max)    

print(new_list [0])

