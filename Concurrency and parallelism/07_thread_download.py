import requests
import time
import threading

def download(url):
  print(f"Downloading from: {url}")
  response = requests.get(url)
  print(f"Response from {url}: {len(response.content)} bytes")

urls = [
 "https://www.httpbin.org/image/jpeg",
 "https://www.httpbin.org/image/png",
 "https://www.httpbin.org/image/svg"
]
start = time.time()
threads = []
for url in urls:
 t = threading.Thread(target=download, args=(url,))
 t.start()
 threads.append(t)

for t in threads:
 t.join()

end = time.time()

print(f"Download took {end - start} seconds")