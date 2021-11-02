def inting(x):
    try:
        return int(x)
    except ValueError:
        return x
