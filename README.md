# Document Similarity Checker using Cosine Similarity

This Python project reads multiple text files, processes the text content, and calculates the **percentage of similarity between documents** using the **cosine similarity** algorithm.

## Features

- Reads and processes multiple `.txt` documents.
- Removes stopwords and non-alphanumeric words.
- Computes term frequency for each document.
- Calculates cosine similarity between every pair of documents.
- Displays a similarity matrix in percentage format.

## How It Works

The script:
1. Loads text content from each file.
2. Preprocesses the content (lowercase + stopword removal).
3. Calculates word frequency per document.
4. Applies cosine similarity to compare all document pairs.
5. Outputs a similarity matrix showing **percentage similarity**.


