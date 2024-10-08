user_input = input("Enter numbers separated by spaces: ")

my_list = [int(num) for num in user_input.split()]

my_tuple = tuple(my_list)

print(my_tuple)
print("Now enter a number you want to check:")
check_num = int(input())
print(check_num in my_tuple)