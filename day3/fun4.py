def connect(**opcje):  # dowolna ilośc danych po nazwie
    print(opcje)


connect()
connect(a=7)
connect(a=7, name="Radek")


# {}
# {'a': 7}
# {'a': 7, 'name': 'Radek'}

def all_args(*args, **kwargs):
    print(f"{args=}")  # args=(1, 2, 3)
    print(f"{kwargs=}")  # kwargs={'a': 1, 'b': 2, 'c': 3}


all_args(1, 2, 3)
all_args(a=1, b=2, c=3)
