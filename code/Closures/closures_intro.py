def outer_func():
    greeting = 'Hello in '

    def inner_func():
        print(greeting + inner_func.__name__ + " but calling in " + outer_func.__name__ )

    inner_func()

outer_func()


def outer_func():
    greeting = 'Hello in '

    def inner_func():
        print(greeting + inner_func.__name__ + " but calling in " + outer_func.__name__ )

    return inner_func

fn = outer_func()
fn()

print(fn.__closure__)
