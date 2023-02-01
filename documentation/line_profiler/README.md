[Source GitHub](https://github.com/pyutils/line_profiler)
```
pip install line_profiler
```

[SO about being able to leave the decorators in the code permanently](https://stackoverflow.com/questions/18229628/python-profiling-using-line-profiler-clever-way-to-remove-profile-statements)

```py
try:
    profile  # type: ignore
except NameError:
    def profile(func):
        return func
```

Or if the environment doesn't have `line_profiler` installed:
```py
try:
    from line_profiler import LineProfiler
    profile = LineProfiler()
except ImportError:
    def profile(func):
        return func
```
