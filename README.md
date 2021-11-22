# pyurify
event processing pipeline
run `python scrape.py | python console.py` in bash.

having both scripts running concurrently requires a bit more setup.
create a fifo with `$ mkfifo connector` then run `$ python console.py < connector` and `python scrape.py > connector` in two different terminals.

### about the Piping
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

We could have some orchestrating python process which spawns threads for both tasks and have them cooperatively yield to eachother. Or just let the scheduler[^1] time-slice them both.
But this complicates the buffering of the data piped between the processes. Let's see if bash can handle that.
Otherwise we can just process the entire pipeline sequentially i.e having `scrape.py` polling some websites for 5 seconds before finishing execution and passing the gathered data to `console.py`.
This could then be called by some orchestrating party every 6 seconds.

- [x] OS level: try spawning 2 python processes and redirect stdout>stdin
    - [ ] try doing it without mkfifo step
- [ ] look into simple [threaded solution](https://docs.python.org/3/library/threading.html#condition-objects)
- [ ] look into generators `yield`


Attempts of trying to redirect something to the stdin of a `python console.py` process the naive way:
![OS-level piping attempt](/assets/proc_stdin.png)
For some reason they get printed to the terminal but not processed by the python script so the timestamp is missing.

[^1]: not sure if this will be the OS scheduler handling or if the python interpreter/runtime(?) has some internal scheduling going on.🤔 
