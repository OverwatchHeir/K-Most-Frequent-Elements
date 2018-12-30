
# Given an array , return the k most frequent element in this array.
# k must be an integer.

from collections import defaultdict

# we create a has map where:
#   key: elements in array ( not duplicates )
#   value : frequency of key in array

# We sort the hash map by values
# We return the k last values

def k_most_frequent(array, k):
    hash_map = defaultdict(int)

    for element in array:
        hash_map[element] += 1

    list = sorted(hash_map.items(), key=lambda x: x[1])

    index = 1
    while index <= k:
        print(list[len(list) - index][0])
        index += 1



k = 2
array = [1, 6, 2, 1, 6, 6]


k_most_frequent(array, k)