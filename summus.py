# Дополнительное практическое задание по модулю: "Подробнее о функциях."
from multiprocessing.pool import job_counter
from types import NoneType

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def summus( ds ):
    if type(ds) == NoneType:
        return 0
    elif type(ds) == str:
        return len(ds)
    elif type(ds) == int or type(ds) == float:
        return ds
    elif type(ds) == list or type(ds) == tuple or type(ds) == set:
        sum = 0
        for i in ds:
            sum += summus(i)
        return sum
    elif type(ds) == dict:
        sum = 0
        for key, i in ds.items():
            sum += summus(key) + summus(i)
        return sum
    else:
        print("что-то пошло не так, неожиданный тип:", type(ds))
        return(0)


print(summus(data_structure ))
