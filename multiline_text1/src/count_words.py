def count_words(text):
    line = text.replace('\n', ' ')
    words = line.split(' ')
    return len(words)
