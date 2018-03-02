

def main():
    f()
    nolan_esplen = Nolan('esplen')
    nolan_esplen.last_name
    pass


def f():
    print('hello world')


class Nolan(object):
    def __init__(self, last_name):
        self.last_name = last_name
        pass

    def f(self):
        print('hello world')


if __name__ == '__main__':
    main()