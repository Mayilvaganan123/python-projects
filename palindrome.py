def palindrome(words):
    words = words.lower()
    li = []
    for w in words:
        li.append(w)
    if li == li[::-1]:
        return True
    return True
words = "A man a plan a canal Panama"
print(palindrome(words))