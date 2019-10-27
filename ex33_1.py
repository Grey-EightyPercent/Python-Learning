# 函数版本
def collect_0_to_SetPoint(set_point):
    i = 0
    numbers = []
    set_point_value = int(set_point)

    while i < set_point_value:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + set_step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers:")
    for num in numbers:
        print(num)

set_point = input("Set point:\t")
set_step = int(input("Set step:\t"))

how_to_form_a_num = collect_0_to_SetPoint(set_point)
print(how_to_form_a_num)
