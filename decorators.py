

PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input ('cual es tu password')

        if password == PASSWORD:
            return func()
        else:
            print('password incorrecto')
    return wrapper

@password_required
def needs_password():
    print('El password es correcto')


def upper(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result.upper()
    return wrapper


@upper
def say_my_name(name):
    return 'Hola,{}'.format(name)
    #print('Hola,{}'.format(name)) # error por no imprimir nada Null

if __name__ == '__main__':
    print(say_my_name('Cesar'))
    #needs_password()
