import sys


def fibonacci(index: int) -> int:
    if index < 2:
        return index
    previous_value = 0
    current_value = 1
    for value in range(1, index):
        tmp = current_value
        current_value += previous_value
        previous_value = tmp
    return current_value


def recursive_fibonacci(index: int) -> int:
    if index < 2:
        return index
    return recursive_fibonacci(index - 1) + recursive_fibonacci(index - 2)


if __name__ == '__main__':
    chosen_index = 20
    if len(sys.argv) > 1:
        chosen_index = sys.argv[1]
    iteration_result = fibonacci(chosen_index)
    recursive_result = recursive_fibonacci(chosen_index)
    print(f"Iteration:\t{iteration_result}\nRecursive:\t{recursive_result}")
