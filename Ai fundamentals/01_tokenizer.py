import tiktoken
import time

text="Hey my name is Rohith!"

start = time.time()
encoder = tiktoken.encoding_for_model("gpt-4o")
encoded_text = encoder.encode(text)
end = time.time()
print(f"{encoded_text} and total time: {end - start}")
decoded_text = encoder.decode(encoded_text)
print(f"{decoded_text}")