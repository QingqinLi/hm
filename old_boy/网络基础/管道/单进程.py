from multiprocessing import Pipe

con1, con2 = Pipe()

con1.send('123')
print(con2.recv())

con2.send("456")
print(con1.recv())