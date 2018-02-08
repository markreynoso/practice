# Algorithms


# Check if two strings are permutations of one another.
# Cracking the Coding interview, page 73
def permutations(str1, str2):
    str1_l = list(str1)
    str2_l = list(str2)
    str1_l.sort()
    str2_l.sort()
    one = ''.join(str1_l)
    two = ''.join(str2_l)
    return one == two

permutations('ysettanum', 'yesmutant')







# Replace spaces with %20 and remove whitespace at the end.
def replace_the_space(string):
    end = string.strip()
    return end.replace(' ', '%20')

replace_the_space('this is a string   ')





# Return letter and count of repeats unless longer than original.
def compress_string(string):
    output = ''
    count = 0
    comp = string[0]
    for idx, letter in enumerate(string):
        if letter == comp:
            count += 1
            if len(string) - 1 == idx:
                output += (comp + str(count))
        elif letter != comp:
            output += (comp + str(count))
            count = 1
            comp = letter
            if len(string) - 1 == idx:
                output += (comp + str(count))
    if len(output) < len(string):
        return output
    else:
        return string

compress_string('aabbbbcccc')








# Rotate matrix 90 degrees.
def rotate_matrix(matrix):
    new_coords = {}
    y_con = len(matrix[0]) - 1
    for x, lst in enumerate(matrix):
        for y, item in enumerate(lst):
            new_coords[item] = (y, y_con - x)
    for key in new_coords:
        m1 = new_coords[key][0]
        m2 = new_coords[key][1]
        matrix[m1][m2] = int(key)
    return matrix

rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])








# is s2 a substring of s1
def is_substring(s1, s2):
    if len(s1) != len(s2):
        return False
    f2l = s2
    for i in range(len(s2)):
        f2l = f2l[1::] + f2l[0]
        if f2l == s1:
            return True
    return False

is_substring('waterbottle', 'erbottlewat')






# Untested - find LinkedList k to last node (recursion)
def k_to_last(node, k, i):
    if node is None:
        return None
    next_node = node.next
    ouput = k_to_last(next_node, k, i)
    i += 1
    if i == k:
        return node
    return output




# Partition a LinkedList at x value. Everything less than x and everything greater than x.
def partition_ll(ll, x):
    current = ll.head
    previous = ll.head
    divider = ll.head
    while current:
        if current.data < x:
            if current is ll.head:
                previous = current
                divider = current
                current = current.next
            else:
                previous.next = current.next
                current.next = divider.next
                divider.next = current
                divider = current
                current = current.next
        else:
            previous = current
            current = current.next
    return ll
