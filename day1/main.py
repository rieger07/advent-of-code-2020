"""
day 1
"""

def find_two_numbers_in_list_sum_to_target(input_list: list, target: int):
    for idx, num1 in enumerate(input_list):
        if idx == len(input_list):
            break
        sliced = input_list[idx+1:]
        for num2 in sliced:
            sum = num1+num2
            if sum == target:
                return (num1, num2)
    raise RuntimeError("No two numbers match target")


def find_three_numbers_in_list_sum_to_target(input_list: list, target: int):
    for idx, num1 in enumerate(input_list):
        if idx == len(input_list)-1:
            break
        sliced = input_list[idx+1:]
        for num2 in sliced:
            sliced2 = input_list[idx+2:]
            for num3 in sliced2:
                s = num1+num2+num3
                if s == target:
                    return (num1, num2, num3)
    raise RuntimeError("No three numbers match target")

def part1():
    TARGET_INT: int = 2020

    with open("day1/input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    nums = list()
    for l in lines:
        nums.append(int(l.strip().rstrip()))
    num1, num2 = find_two_numbers_in_list_sum_to_target(nums, TARGET_INT)
    print(num1, num2, num1*num2)


def part2():
    TARGET_INT: int = 2020

    with open("day1/input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    nums = list()
    for l in lines:
        nums.append(int(l.strip().rstrip()))
    num1, num2, num3 = find_three_numbers_in_list_sum_to_target(nums, TARGET_INT)
    print(num1, num2, num3, num1*num2*num3)

if __name__ == "__main__":
    #part1()
    part2()
