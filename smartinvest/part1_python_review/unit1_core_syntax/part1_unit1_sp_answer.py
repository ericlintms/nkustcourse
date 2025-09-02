def process_numbers(numbers):
    """
    計算數字列表的總和，印出結果，
    並回傳只包含偶數的新列表。
    """
    total = sum(numbers)
    print(f"The sum of the list is: {total}")

    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# 範例
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = process_numbers(my_list)
print(f"The even numbers are: {evens}")
