 """Boggle. Matrix of r rows and c columns.

Find the number of possible words in matrix."""

"""Example:
[[j, e, l, a, p],
 [a, g, w, q, i],
 [m, b, e, u, t],
 [p, r, y, l, k]]"""

"""Goal:

Iterate through the list of lists. Do a breadth-first-search from each letter to determine how many possible words there are.

I'll need a holder list for the BFS, a holder list for words (likely a set to remove duplicates)."""

 def boggle_word_finder(matrix, is_word):
    words = []
    for i in range(len(matrix) - 1):
        for j, letter in enumerate(matrix[i]):
            BFS(i, j, is_word)

def BFS(matrix, i, j, is_word):

    bfs_stack = Stack()
    """check +1 in each direction, then check if is_word, then push into stack and do bfs on last letter of each potential word, making sure not to use any coords in word already."""
    
