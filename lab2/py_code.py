def min_edit_distance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    # Create a 2D array to store the distances
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    # Initialize the first row and column
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[len1][len2]

def get_user_input():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    max_length = 100  # Maximum allowed length for input words

    if len(word1) >= max_length or len(word2) >= max_length:
        print(f"Error: Input words are too long. Maximum allowed length is {max_length} characters.")
        return None, None

    return word1, word2

if __name__ == "__main__":
    word1, word2 = get_user_input()

    if word1 is not None and word2 is not None:
        distance = min_edit_distance(word1, word2)
        print(f"Levenshtein distance between '{word1}' and '{word2}' is {distance}")

