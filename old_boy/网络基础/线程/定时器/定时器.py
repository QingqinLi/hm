from threading import Timer


def func():
    print("2 seconds")


if __name__ == '__main__':
    Timer(2, func).start()