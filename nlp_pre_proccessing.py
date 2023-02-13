#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Function to preprocess text data
def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if not word in stop_words]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Join tokens back into a string
    processed_text = " ".join(tokens)
    
    return processed_text

# Function to upload file and preprocess text
def upload_file():
    # Open file dialog to select file
    file_path = filedialog.askopenfilename()
    
    # Read file content
    with open(file_path, "r") as file:
        text = file.read()
        text_area.insert("1.0", text)
    
    # Preprocess text data
    processed_text = preprocess_text(text)
    
    # Display preprocessed text in GUI
    result_label.config(text=processed_text)

# Function to save preprocessed text as a file
def save_file():
    # Open file dialog to select file path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    
    # Write preprocessed text to file
    with open(file_path, "w") as file:
        file.write(result_label.cget("text"))

# GUI window
root = tk.Tk()
root.geometry("800x600")
root.title("Text Data Preprocessing for NLP")

text_area = tk.Text(root, wrap="word")
text_area.pack(fill="both", expand=True)


# Upload file button
upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack()


# Result label to display preprocessed text
result_label = tk.Label(root, text="")
#result_label.pack()

# Save file button
save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack()

# Start GUI event loop
root.mainloop()

