def custom_function(*args, **kwargs) -> None:
    print(f"We have {len(args)} positional arguments: {args}")
    print(f"We have {len(kwargs)} positional arguments: {kwargs}")