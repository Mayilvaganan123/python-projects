def freq(words):
    words = words.lower()
    seen = {}
    for word in words:
        if word in seen:
            seen = seen.get(word, 0) + 1
        else:
            seen.add(word)
    return seen
words = "the cat and the dog and the bird"
print(freq(words))