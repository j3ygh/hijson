# hijson
 
A pratice to implement `json.loads` and `json.dumps` by myself. This is not well-tested.

## Play with it

After cd to this repo's root and run `python3`.
```
Python 3.8.11 (default, Jun 29 2021, 03:08:07) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from json_parsers import stringify
>>> dct = {"age": 29, "name": "Jimmy", "friend_names": ["Charlie", "Shelly"]}
>>> stringify(dct)
'{"age": 29, "name": "Jimmy", "friend_names": ["Charlie", "Shelly"]}'
```

## Run some tests on it
```
python3 run_accuracy_tests.py
```

You want to do some performance tests on it, too.
```
python3 run_performance_tests.py
```

