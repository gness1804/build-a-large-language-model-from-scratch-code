import torch
from data_loader import create_dataloader_v1
from file_utils import download_and_read_text_file

raw_text = download_and_read_text_file(
    file_path="the-verdict.txt",
    url=("https://raw.githubusercontent.com/rasbt/"
         "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
         "the-verdict.txt")
)

vocab_size = 50257
output_dim = 256

token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)

max_length = 4
dataloader = create_dataloader_v1(
    raw_text, batch_size=8, max_length=max_length,
    stride=max_length, shuffle=False
)
data_iter = iter(dataloader)
inputs, targets = next(data_iter)

# print("Token IDs:\n", inputs)
# print("\nInputs shape:\n", inputs.shape)

token_embeddings = token_embedding_layer(inputs)
# print(token_embeddings.shape)

# uncomment & execute the following line to see how the embeddings look like
# print(token_embeddings)

context_length = max_length
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)

# uncomment & execute the following line to see how the embedding layer weights look like
# print(pos_embedding_layer.weight)

pos_embeddings = pos_embedding_layer(torch.arange(max_length))
# print(pos_embeddings.shape)

# uncomment & execute the following line to see how the embeddings look like
# print(pos_embeddings)

input_embeddings = token_embeddings + pos_embeddings
print(input_embeddings.shape)

# uncomment & execute the following line to see how the embeddings look like
# print(input_embeddings)