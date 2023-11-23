import re
import doctest


def check_password(password):
    # Проверка на длину не менее 6 символов
    if len(password) < 6:
        return False

    # Проверка наличия хотя бы двух латинских символов в верхнем регистре
    if len(re.findall(r'[A-Z]', password)) < 2:
        return False

    # Проверка наличия хотя бы одной цифры
    if not re.search(r'\d', password):
        return False

    # Проверка наличия хотя бы двух различных специальных символов
    special_chars = r'^$%@#&*!?'
    if len(re.findall(r'[' + re.escape(special_chars) + ']', password)) < 2:
        return False

    # Проверка на отсутствие трех одинаковых символов подряд
    if re.search(r'(.)\1\1', password):
        return False

    # Если все проверки пройдены, возвращаем True (пароль корректный)
    return True



def test_check_password():
    '''
    >>> check_password('rtG3FG!Tr^e')
    True
    >>> check_password('aA1!*!1Aa')
    True
    >>> check_password('oF^a1D@y5e6')
    True
    >>> check_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>> check_password('1DE$%паароль')
    True
    >>> check_password('1DE$паро#ль')
    True
    >>> check_password('пароль')
    False
    >>> check_password('password')
    False
    >>> check_password('qwerty')
    False
    >>> check_password('lOngPa$$$W0Rd')
    False
    >>> check_password('Pass-3@@')
    False
    >>> check_password('l232DE')
    False

    '''
    pass

password = '1DE$паро#ль';
print(check_password(password))
if __name__ == "__main__":
    doctest.testmod(verbose=True)