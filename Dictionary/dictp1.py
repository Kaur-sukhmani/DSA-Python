
"""Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}
 """
# Read from the file words.txt and output the word frequency list to stdout.
def count_freq(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1 
        else:
            word_freq = 1
    return word_freq
    
# SPACE COMPLEXITY -> O(N)
# TIME COMPLEXITY -> O(N)

