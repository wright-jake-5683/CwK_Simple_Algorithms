import random

def create_list():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(-1000, 1000))
    return numbers

def swap(list, item1, item2):
    temp = list[item1]
    list[item1] = list[item2]
    list[item2] = temp

def bubble_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        while j >= 0:
            if list[j + 1] < list[j]:
                swap(list, j+1, j)
            j -= 1

def main():
    random_list = create_list()
    print(f"Unsorted List: {random_list} \n")

    bubble_sort(random_list)
    print(f"Sorted List: {random_list} ")

main()