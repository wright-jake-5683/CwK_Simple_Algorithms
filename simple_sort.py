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

def simple_sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j
        swap(list, min, i)



def main():
    random_list = create_list()
    print(f"Unsorted List: {random_list} \n")
    simple_sort(random_list)
    print(f"Sorted List: {random_list} ")

main()