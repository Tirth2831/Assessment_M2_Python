'''
 Write a Python program to count the occurrences of each word in a
given sentence
'''
sentence = "Tops is the best Tops is great"

words = sentence.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)
