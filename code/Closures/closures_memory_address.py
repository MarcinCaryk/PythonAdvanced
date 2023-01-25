def outer_func():
    greeting = 'Hello in '
    print(hex(id(greeting)))

    def inner_func():
        print(greeting + inner_func.__name__ + " but calling in " + outer_func.__name__ )
        print(hex(id(greeting)))

    return inner_func

fn = outer_func()
fn()

print(fn.__code__.co_freevars)