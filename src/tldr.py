from gpt4all import GPT4All
from webscraper import webscraper

model = GPT4All("GPT4All-13B-snoozy.ggmlv3.q4_0.bin")
output = model.generate(f"Write a TLDR for this article: {webscraper()}", max_tokens=4092, temp=0.7, top_k=40, top_p=0.4, repeat_penalty=1.18, repeat_last_n=64, n_batch=8, n_predict=None, streaming=False)


print("OUTPUT: \n",output)
