def printer():
    while True:
        try:
            i = yield
            print(i)
        except ValueError:
            print('******')
        except GeneratorExit:
            print('The end')
            break


p = printer()

next(p)

p.send(5)
p.send(7)
p.send(7)

p.throw(ValueError)

p.close()