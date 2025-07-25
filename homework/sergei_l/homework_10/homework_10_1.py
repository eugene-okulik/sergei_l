def end_line(func):

    def wrapper(text):
        func(text)
        print("finished")

    return wrapper


@end_line
def sample_func(text):
    print(text)


sample_func("This is a sample function")
