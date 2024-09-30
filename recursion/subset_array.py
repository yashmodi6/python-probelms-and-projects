# General Idea:
# Example: [1, 2]
#
# For each element, we have two choices:
# 1. Take the element
# 2. Don't take the element
#
# Example:
# Take 1 → [1]
#   ├── Take 2 → [1, 2]
#   └── Don't take 2 → [1]
#
# Don't take 1 → []
#   ├── Take 2 → [2]
#   └── Don't take 2 → []


array = ["1", "2", "3", "4"]


def generate_subsets(array, index, current):

    # if index has reached end
    # then we have explored all possibilities of this branch
    if index == len(array):
        print(current)
        return

    # Take the item
    current.append(array[index])
    generate_subsets(array, index + 1, current)

    # undo
    current.pop()

    # remove the item
    generate_subsets(array, index + 1, current)


generate_subsets(array, 0, [])
