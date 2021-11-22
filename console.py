import time
import sys

# logs input to console with a timestamp
# try `echo "hello" | python console.py`.sh
# for line in sys.stdin:
#     print(time.ctime(),line)
while True:
    line = sys.stdin.readline()
    if not line:
        break
    sys.stdout.write(time.ctime())
    sys.stdout.write(':'+line)
    sys.stdout.flush()
