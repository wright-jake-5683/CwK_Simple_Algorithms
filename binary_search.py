import random

def create_list():
    nums = []
    for i in range(10):
        nums.append(random.randint(-1000, 1000))
    return nums

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


def binary_search(list, low, high, target):
    while low <= high:
        middle = (low + high) // 2

        if list[middle] == target:
            return middle
        
        elif list[middle] < target:
            low = middle + 1

        elif list[middle] > target:
            high = middle - 1

    return -1

def main():
    random_list = create_list()
    print(f"Unsorted List: {random_list} \n")
    bubble_sort(random_list)
    print(f"Sorted List: {random_list} \n")

    number = int(input("What number do you want to search for? \n"))
    search_result_index = binary_search(random_list, 0, len(random_list) - 1, number)
    if search_result_index == -1:
        print(f"{number} is not found inside the searched list \n")
    else:
        print(f"{number} is at index {search_result_index} of the list \n")