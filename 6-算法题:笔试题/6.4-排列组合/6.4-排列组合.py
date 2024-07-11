# Python内置库 itertools
from itertools import permutations

def get_all_permutations(elements, length):
    all_permutations = []
    for p in permutations(elements, length):
        all_permutations.append(''.join(p))
    return all_permutations

# 测试代码
elements = 'abc'
length = 3

permutations = get_all_permutations(elements, length)

for permutation in permutations:
    print(permutation)


# 递归
def find_combinations(elements, length, current_combination, all_combinations):
    if length == 0:
        all_combinations.append(','.join(current_combination))
        return

    for element in elements:
        current_combination.append(element)
        find_combinations(elements, length - 1, current_combination, all_combinations)
        current_combination.pop()

def get_all_combinations(elements, length):
    all_combinations = []
    find_combinations(elements, length, [], all_combinations)
    return all_combinations

# 测试代码
elements = 'abc'
length = 3

combinations = get_all_combinations(elements, length)

for combination in combinations:
    print(combination)