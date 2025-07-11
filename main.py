import os
import urllib.request
import re
import tiktoken

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

all_tokens: list[str] = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
vocab_size: int = len(all_tokens)

base_vocab: dict[str, int] = {token: index for index, token in enumerate(all_tokens)} # The Python dictionary that maps each word to its corresponding index

class SimpleTokenizerV2:
    def __init__(self, base_vocab: dict[str, int]):
        self.str_to_int = base_vocab
        self.int_to_str = {i:s for s,i in base_vocab.items()}
    
    def encode(self, text: str) -> list[int]:
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
                                
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        preprocessed = [
            item if item in self.str_to_int 
            else "<|unk|>" for item in preprocessed
        ]
        ids: list[int] = [self.str_to_int[s] for s in preprocessed]
        return ids
        
    def decode(self, ids: list[int]) -> str:
        text: str = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text
    
tokenizer: SimpleTokenizerV2 = SimpleTokenizerV2(base_vocab)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."

text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)

tokenizer2 = tiktoken.get_encoding("gpt2")

integers = tokenizer2.encode(text, allowed_special={"<|endoftext|>"})

# print(integers)

strings = tokenizer2.decode(integers)

print(strings)

# text = " <|endoftext|> ".join((text1, text2))

# print(tokenizer.decode(tokenizer.encode(text)))