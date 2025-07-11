import os
import urllib.request
import re

if not os.path.exists("the-verdict.txt"):
    url = ("https://raw.githubusercontent.com/rasbt/"
           "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
           "the-verdict.txt")
    file_path = "the-verdict.txt"
    urllib.request.urlretrieve(url, file_path)

    print(f"File downloaded to {file_path}")

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
    
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_tokens = sorted(set(preprocessed))
vocab_size = len(all_tokens)

token_to_index = {token: index for index, token in enumerate(all_tokens)} # The Python dictionary that maps each word to its corresponding index
index_to_token = {index: token for index, token in enumerate(all_tokens)} # The Python dictionary that maps each index to its corresponding word

print(token_to_index["the"])
print(index_to_token[1])
