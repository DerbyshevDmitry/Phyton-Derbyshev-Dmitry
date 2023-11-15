def validate_args(func):
    def wrapper(*args):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"

        arg = args[0]
        if not isinstance(arg, int):
            return "Wrong types"
        elif arg < 0:
            return "Negative argument"

        return func(*args)

    return wrapper



@validate_args
def example_function(x):
    return f"Argument {x} is valid"



print(example_function(5))
print(example_function())
print(example_function(2, 3))
print(example_function("a"))
print(example_function(-1))