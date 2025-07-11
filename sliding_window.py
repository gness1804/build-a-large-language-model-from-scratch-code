import tiktoken
from file_utils import download_and_read_text_file

tokenizer = tiktoken.get_encoding("gpt2")

raw_text = download_and_read_text_file(
    file_path="the-verdict.txt",
    url=("https://raw.githubusercontent.com/rasbt/"
         "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
         "the-verdict.txt")
)

enc_text = tokenizer.encode(raw_text)

enc_sample = enc_text[50:]

context_size = 4
# x = enc_sample[:context_size]
# y = enc_sample[1:context_size + 1]

# print(x)
# print(y)

for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]

    print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))



