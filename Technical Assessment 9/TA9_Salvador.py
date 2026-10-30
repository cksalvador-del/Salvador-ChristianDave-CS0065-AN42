
# ==========================================
# 1. IMPORTING DEPENDENCIES AND DATA
# ==========================================

import pandas as pd
import sqlite3
import regex as re
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Create dataframe from CSV
df = pd.read_csv('emails.csv')

df.head()


# ==========================================
# 2. EXPLORATORY ANALYSIS
# ==========================================

print("spam count: " + str(len(df.loc[df.spam == 1])))
print("not spam count: " + str(len(df.loc[df.spam == 0])))

print(df.shape)

df['spam'] = df['spam'].astype(int)

# Remove duplicate rows
df = df.drop_duplicates()

df = df.reset_index(inplace=False)[['text', 'spam']]

print(df.shape)


# ==========================================
# 3. CLEANING THE TEXTS
# ==========================================

clean_desc = []

for w in range(len(df.text)):

    desc = df['text'][w].lower()

    # Remove punctuation
    desc = re.sub('[^a-zA-Z]', ' ', desc)

    # Remove tags
    desc = re.sub("&lt;/?.*?&gt;", " ", desc)

    # Remove digits and special characters
    desc = re.sub(r"(\d|\W)+", " ", desc)

    clean_desc.append(desc)


# Assign the cleaned descriptions to the dataframe
df['text'] = clean_desc

df.head(3)


# ==========================================
# 4. REMOVING STOP WORDS
# ==========================================

stop_words = [
    'is', 'you', 'your', 'and', 'the', 'to', 'from',
    'or', 'I', 'for', 'do', 'get', 'not', 'here',
    'in', 'im', 'have', 'on', 're', 'new', 'subject'
]

# Remove stop words from the text
df['text'] = df['text'].apply(
    lambda x: ' '.join(
        [word for word in x.split() if word not in stop_words]
    )
)


# ==========================================
# 5. CONSTRUCT THE WORD CLOUD
# ==========================================

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='black',
    stopwords=stop_words,
    max_words=1000,
    min_font_size=20
).generate(str(df['text']))


# Plot the word cloud
fig = plt.figure(figsize=(8, 8), facecolor=None)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# Save the generated word cloud
wordcloud.to_file("spam_wordcloud.png")

print("Word Cloud successfully generated!")
