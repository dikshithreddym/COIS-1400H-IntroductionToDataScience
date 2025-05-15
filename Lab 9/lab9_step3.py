# Dikshith Reddy M
# Student id: 0789055

import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist
import string

# Ensure you have these downloaded
nltk.download('gutenberg')
nltk.download('stopwords')

# Load Macbeth from the Gutenberg collection
macbeth_words = gutenberg.words('shakespeare-macbeth.txt')

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Create a set of punctuation
punctuation = set(string.punctuation)

# Filter out stopwords and punctuation from Macbeth
filtered_words = [word.lower() for word in macbeth_words if word.lower() not in stop_words and word not in punctuation]

# Get frequency distribution
freq_dist = FreqDist(filtered_words)

# Display the 15 most common words
for word, frequency in freq_dist.most_common(15):
    print(word, frequency)
