
import re
from collections import Counter

# Define the path to your .txt file
txt_file_path = '/Users/binodmaharjan/Downloads/Assignment 2 actual csvs/output text2/combined_text.txt'

# Read the content of the text file
with open(txt_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Clean and preprocess the text
# Convert to lowercase, remove punctuation and special characters, and split by spaces
# Only keep words with 2 or more characters (and exclude numbers)
words = re.findall(r'\b[a-zA-Z]{2,}\b', text.lower())

# Count the occurrences of each word
word_counts = Counter(words)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Display the top 30 words with their counts
for word, count in top_30_words:
    print(f"{word}: {count}")
