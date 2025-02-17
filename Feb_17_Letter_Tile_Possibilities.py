"""
Letter Tile Possibilities:
Approach: 
    The problem simply boils down to finding all the possible permutations of the given string but 
    the catch is that we need to store all the substrings for each permutation and return the count 
    of all the unique substrings for each permutation.
    I used backtracking to solve this problem, where I am trying to find all the possible permutations


Time Complexity: 
    O(n * n!) where n is the input string, as we are checking all the possible permutations of the given string and
    for each permutation we are storing all the substrings of the permutation which is n complexity.
Space Complexity: 
    O(n) where n is the input string, as we are using a visited array of size n and a permute array of size n.
"""


def get_all_permutations(tiles, visited, sequences, permute):
    sequences.add("".join(permute))
    for i in range(len(tiles)):
        if visited[i] == False:
            visited[i] = True
            permute.append(tiles[i])
            get_all_permutations(tiles, visited, sequences, permute)
            visited[i] = False
            permute.pop()



def numTilePossibilities(tiles: str) -> int:
    sequences = set()
    visited = [False] * len(tiles)
    get_all_permutations(tiles, visited, sequences, [])
    return len(sequences)-1
    
    

if __name__ == "__main__":
    print(numTilePossibilities("AAB")) #8