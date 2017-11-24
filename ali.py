
def test(*args, **kwargs):
    print(kwargs)
    # say(a=1, b=2)
    say(**kwargs)


def say(a, b):
    print(a)

test(a=1, b=2)

