from multiprocessing import Event

e = Event()
# print(e.set())
# print(e.clear())
# print(e.wait())
# print(e.is_set())

print(e.is_set())
e.set()
e.wait()
print(e.is_set())
print(123)
e.clear()
print(e.is_set())
e.wait()
print(333)