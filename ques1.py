def sort_and_remove_duplicates(numbers):
    sorted_list = sorted(set(numbers))
    return sorted_list

def main():
    try:
        user_input = "1 9 2 7 1 9"  # Sample input
        numbers = list(map(int, user_input.split()))
        result = sort_and_remove_duplicates(numbers)
        print("The Sorted Non-Duplicate List:", result)
    except ValueError:
        print("Invalid input. Please enter space-separated integers only.")

if __name__ == "__main__":
    main()
