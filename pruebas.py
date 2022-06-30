def check_palindrome(word):
    return [c for c in word] == [word[i] for i in range(-1, -len(word) - 1, -1)]

word = input("Enter word: \n")
print(f"{word} is a palindrome" if check_palindrome(word) else f"{word} isn't a palindrome.")