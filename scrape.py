import time

# mock scrape which writes to stdout every second
for _ in range(5):
    print("I found a new blog post!")
    time.sleep(1)
