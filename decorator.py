import datetime

def decorator(func):

    def inner(*args, **kwargs):
        print(datetime.datetime.now())
        result = func(*args)
        print(datetime.datetime.now())
        return result
    return inner

def summarize(a: int, b:int) -> int:
    return a + b

@decorator
def summarize_with_decorator(a: int, b:int) -> int:
    return a + b


"""чтобы вызвать мог на выбор вызывать или просто функцию, или функцию с декоратором"""
print("Просто функция", summarize(1, 4))
new_sum = decorator(summarize)
print("Функция с декоратором", new_sum(2, 4))

"""тут всегда функция будет в обертке декоратора, отдельно не вызвать,
то есть если я сверху функции указал @decorator, то отдельно функцию не вызывать
"""
print("Функция с декоратором, которая без него не может", summarize_with_decorator(3, 7))
