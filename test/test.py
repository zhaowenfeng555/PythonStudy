def f():
    try:
        x = 1/0
        print('running try')
        # return 1
    except:
        print('running except')
        return 2
    else:
        print('running else')
        return 3
    finally:
        print('running finally')
        return 4

print(f())
