def solution(S):

    # create a hash map to store the occurance of all letters in ASCII code
    # 65: A, 97: a
    # Space Complexity: O(1)
    hash_map = {i: False for i in list(range(65, 91)) + list(range(97, 123))}

    # update the hash map to check if the character exists
    # Time complexity: O(N)
    for char in S:
        if not hash_map[ord(char)]:
            hash_map[ord(char)] = True

    largest = 0  # for storing the ASCII code of the largest letter

    # Time complexity: O(N)
    for char in S:

        # only check the uppercase and skip the lowercase
        if ord(char) >= 91:
            continue

        # if both the uppercase and lowercase occur in S
        if hash_map[ord(char)] and hash_map[ord(char) + 32]:
            if ord(char) > largest:
                largest = ord(char)

    return chr(largest) if largest != 0 else 'NO'

S = 'aaBabcDaA'
print(solution(S))
