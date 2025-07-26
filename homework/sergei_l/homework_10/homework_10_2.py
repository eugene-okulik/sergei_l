def counts(count=1):

    def repeat_function(func):

        def wrapper(text):
            for _ in range(count):
                result = func(text)
            return result

        return wrapper

    return repeat_function


@counts(count=3)
def sample_function(text):
    print(text)


sample_function("This is a sample function")
