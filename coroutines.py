def auto_prime(f):

    def wrapper(*args, **kwargs):
        coro = f(*args, **kwargs)
        next(coro)
        return coro

    return wrapper


@auto_prime
def print_number():
    result = []
    while True:
        number = yield
        if number is None:
            break
        print(number)
        result.append(number)
    return result


@auto_prime
def print_and_yield_number():
    result = []
    while True:
        number = yield
        if number is None:
            break
        result.append(number)
        yield number
    return result


@auto_prime
def multiply_number_by_var(var):
    while True:
        number = yield
        print(number * var)


def terminate_coroutine(corot):
    try:
        corot.send(None)
    except StopIteration as exc:
        return exc.value


@auto_prime
def coroutine_to_coroutines(c1, c2):
    first = c1()
    last = c2()
    while True:
        name = yield
        if name is None:
            break
        str_list = name.split(' ')
        first.send(str_list[0])
        last.send(str_list[1])
    return terminate_coroutine(first), terminate_coroutine(last)


@auto_prime
def get_list_of_names():
    result = []
    while True:
        name = yield
        if name is None:
            break
        result.append(name)
    return result
