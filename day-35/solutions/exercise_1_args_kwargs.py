def describe_call(*args, **kwargs):
    print(args)
    print(kwargs)


describe_call(1, 2, 3, name="Ada", age=30)
