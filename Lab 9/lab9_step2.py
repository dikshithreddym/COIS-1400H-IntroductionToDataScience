# Dikshith Reddy M
# Student id: 0789055

import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.probability import FreqDist

# Ensure you have these downloaded
nltk.download('gutenberg')
nltk.download('stopwords')

# Load Macbeth from the Gutenberg collection
macbeth_words = gutenberg.words('shakespeare-macbeth.txt')

# Load English stopwords
stop_words = set(stopwords.words('english'))

# Filter out stopwords from Macbeth
filtered_words = [word.lower() for word in macbeth_words if word.lower() not in stop_words]

# Get frequency distribution
freq_dist = FreqDist(filtered_words)

# Display the 15 most common words
for word, frequency in freq_dist.most_common(15):
    print(word, frequency)
