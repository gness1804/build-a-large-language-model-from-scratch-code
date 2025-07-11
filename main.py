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

base_vocab = {token: index for index, token in enumerate(all_tokens)} # The Python dictionary that maps each word to its corresponding index
# index_to_token = {index: token for index, token in enumerate(all_tokens)} # The Python dictionary that maps each index to its corresponding word

# print(token_to_index["the"])
# print(index_to_token[1])

class SimpleTokenizerV1:
    def __init__(self, base_vocab):
        self.str_to_int = base_vocab
        self.int_to_str = {i:s for s,i in base_vocab.items()}
    
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
                                
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
tokenizer = SimpleTokenizerV1(base_vocab)

text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
