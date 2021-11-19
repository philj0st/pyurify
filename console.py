import time
import sys

# logs input to console with a timestamp
# try `echo "hello" | python console.py`.sh
for line in sys.stdin:
    print(time.ctime(),line)
