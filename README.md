# pyurify
event processing pipeline
run `python scrape.py | python console.py` in bash.

### Piping
When bashing `python scrape.py | python console.py` with the most naive implementation of 
```
while True:
  print("new event")
  time.sleep(1)
```
and
```
for line in sys.stdin:
    print(time.ctime(),line)
```
we run into the problem that `scrape.py` must finish execution before bash can pipe it's output to `console.py`.
We could have some orchestrating process who spawns threads for both and let the scheduler time-slice them both. This complicates the buffering of the bash piping. Let's see if bash can handle that.
Otherwise we can just process the entire pipeline sequentially i.e having `scrape.py` polling some websites for 5 seconds before finishing execution and passing the gathered data to `console.py`.
This could then be called by some orchestrating party every 6 seconds.

- [ ] OS level: try spawning 2 python processes and redirect stdout>stdin
- [ ] look into simple [threaded solution](https://docs.python.org/3/library/threading.html#condition-objects)
- [ ] look into generators `yield`

```
for line in sys.stdin:
    print(time.ctime(),line)
```

Attempts of trying to redirect something to the stdin of a `python console.py` process the naive way:
![OS-level piping attempt](/assets/proc_stdin.png)
For some reason they get printed to the terminal but not processed by the python script so the timestamp is missing.
