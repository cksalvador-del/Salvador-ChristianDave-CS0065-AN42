import pandas as pd
import sqlite3
import regex as re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pathlib import Path

# Set the dataset directory
folder = Path("sorted_data_acl")

# Store all collected reviews
review_list = []

# Load positive and negative reviews
for path in folder.rglob("*.review"):

    review_type = path.stem

    if review_type not in ["positive", "negative"]:
        continue

    with open(path, "r", encoding="latin-1") as f:
        data = f.read()

    # Get the review text from the file
    extracted_reviews = re.findall(
        r"<review_text>(.*?)</review_text>",
        data,
        flags=re.DOTALL | re.IGNORECASE
    )

    for item in extracted_reviews:
        review_list.append({
            "text": item,
            "sentiment": review_type
        })

# Convert collected reviews into a DataFrame
df = pd.DataFrame(review_list)

# Display the number of reviews
print("\nREVIEW SUMMARY")
print("-------------------------")
print("Total positive reviews:", len(df[df["sentiment"] == "positive"]))
print("Total negative reviews:", len(df[df["sentiment"] == "negative"]))
print("Original dataset size:", df.shape)

# Remove duplicate reviews
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

print("Dataset after removing duplicates:", df.shape)

# Text preprocessing
processed_reviews = []

for index in range(len(df)):

    text = df.loc[index, "text"].lower()

    # Remove punctuation and unnecessary symbols
    text = re.sub("[^a-zA-Z]", " ", text)

    # Remove HTML tags
    text = re.sub("&lt;/?.*?&gt;", " ", text)

    # Remove numbers and special characters
    text = re.sub(r"(\d|\W)+", " ", text)

    processed_reviews.append(text)

# Update the DataFrame with cleaned text
df["text"] = processed_reviews

# List of stop words
stop_words = [
    "is", "you", "your", "and", "the", "to", "from", "or",
    "i", "for", "do", "get", "not", "here", "in", "im",
    "have", "on", "re", "new", "subject"
]

# Create a word cloud containing all reviews
all_reviews = " ".join(df["text"])

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="black",
    stopwords=stop_words,
    max_words=1000,
    min_font_size=20
).generate(all_reviews)

# Show and save the overall word cloud
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("challenge_wordcloud.png", bbox_inches="tight")
plt.show()

# Create individual word clouds for each sentiment
sentiment_types = ["positive", "negative"]

for review_type in sentiment_types:

    selected_reviews = " ".join(
        df.loc[df["sentiment"] == review_type, "text"]
    )

    if selected_reviews.strip():

        cloud = WordCloud(
            width=800,
            height=800,
            background_color="black",
            stopwords=stop_words,
            max_words=1000,
            min_font_size=20
        ).generate(selected_reviews)

        # Display the generated word cloud
        plt.figure(figsize=(8, 8))
        plt.imshow(cloud)
        plt.axis("off")
        plt.title(review_type.capitalize() + " Reviews")

        # Save the word cloud image
        plt.savefig(
            review_type + "_wordcloud.png",
            bbox_inches="tight"
        )

        plt.show()
