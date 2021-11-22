import time
import sys

# mock scrape which writes to stdout every second
for _ in range(5):
    line = "I found a new blog post!\n"
    sys.stdout.write(line)
    sys.stdout.flush()
    time.sleep(1)
