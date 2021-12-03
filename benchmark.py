import json
import ujson
import hijson

from timeit import timeit
from sample_values import values
from pandas import DataFrame

NUMBER = 10000
NDIGITS = 4


def get_func_without_arg(func, *args, **kwargs):
    def func_without_arg():
        return func(*args, **kwargs)

    return func_without_arg


libs = {
    "json": {"dumps": json.dumps},
    "ujson": {"dumps": ujson.dumps},
    "hijson": {"dumps": hijson.dumps},
}

columns = list(libs.keys())
rows = []
for value in values:
    row = []
    for lib, funcs in libs.items():
        dumps_func = funcs["dumps"]
        func_without_arg = get_func_without_arg(dumps_func, value)
        time = timeit(func_without_arg, number=NUMBER)
        row.append(round(time, NDIGITS))
    rows.append(row)

df = DataFrame(rows, columns=columns)
print(df)
