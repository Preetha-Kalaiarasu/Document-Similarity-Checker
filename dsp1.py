import math
from collections import Counter
from nltk.corpus import stopwords

# Download stopwords
import nltk
nltk.download('stopwords', quiet=True)

# Preprocessing function: Tokenizes, lowers the text, and removes stopwords
def preprocess_text(text):
    # Convert text to lowercase and split by spaces
    tokens = text.lower().split()
    
    # Remove stopwords and non-alphanumeric tokens
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    
    return tokens

# Compute the term frequency for each document
def compute_term_frequency(tokens):
    return Counter(tokens)

# Compute cosine similarity between two term frequencies
def cosine_similarity(freq1, freq2):
    # Get all the unique words from both documents
    all_words = set(freq1.keys()).union(set(freq2.keys()))
    
    # Calculate dot product and magnitudes
    dot_product = sum([freq1.get(word, 0) * freq2.get(word, 0) for word in all_words])
    magnitude1 = math.sqrt(sum([freq1.get(word, 0) ** 2 for word in all_words]))
    magnitude2 = math.sqrt(sum([freq2.get(word, 0) ** 2 for word in all_words]))
    
    # Calculate cosine similarity
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)
def read_and_preprocess_files(file_paths):
    documents = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            tokens = preprocess_text(text)
            documents.append(tokens)
    return documents

# Main function to compute similarities between documents
def main(file_paths):
    # Read and preprocess files
    documents = read_and_preprocess_files(file_paths)
    
    # Compute term frequencies for each document
    term_frequencies = [compute_term_frequency(doc) for doc in documents]
    
    # Calculate cosine similarity between all document pairs
    num_files = len(file_paths)
    similarity_matrix = [[0] * num_files for _ in range(num_files)]
    
    for i in range(num_files):
        for j in range(i, num_files):
            sim = cosine_similarity(term_frequencies[i], term_frequencies[j])
            similarity_matrix[i][j] = sim
            similarity_matrix[j][i] = sim
    
    # Display the similarity results
    print("\nDocument Similarity Matrix (Cosine Similarity):")
    for i in range(num_files):
        for j in range(num_files):
            print(f"Similarity between {file_paths[i]} and {file_paths[j]}: {similarity_matrix[i][j] * 100:.2f}%")
    
    return similarity_matrix

# Specify the text files to compare
file_paths = [
    r'C:\Users\preet\OneDrive\Documents\file1.txt',  
    r'C:\Users\preet\OneDrive\Documents\file2.txt',
    r'C:\Users\preet\OneDrive\Documents\file3.txt',
    r'C:\Users\preet\OneDrive\Documents\file4.txt',  
]

# Call the main function
main(file_paths)
