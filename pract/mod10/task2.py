import re
import doctest

def check_web_color(color):

    # Регулярное выражение для проверки rgb формата
    rgb_pattern = r'^rgb\((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0?\d{1,2})%?,\s*(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0?\d{1,2})%?,\s*(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0?\d{1,2})%?\)$'

    # Регулярное выражение для проверки hex формата
    hex_pattern = r'^#([a-fA-F\d]{3}){1,2}$'

    # Регулярное выражение для проверки hsl формата
    hsl_pattern = r'^hsl\((\d{1,3}|[1-2]\d{2}|3[0-5]\d|360),\s*(\d{1,2}|100)%,\s*(\d{1,2}|100)%\)$'

    # Проверяем переданную строку на соответствие любому из трех форматов
    if re.match(rgb_pattern, color) or re.match(hex_pattern, color) or re.match(hsl_pattern, color):
        return True
    else:
        return False

def test_check_web_color():
    """


    # Корректные цвета
    >>> check_web_color('#21f48D')
    True
    >>> check_web_color('#888')
    True
    >>> check_web_color('#212422')
    True
    >>> check_web_color('rgb(255, 255,255)')
    True
    >>> check_web_color('rgb(0, 0, 0)')
    True
    >>> check_web_color('rgb(10%, 20%, 0%)')
    True
    >>> check_web_color('hsl(200,100%,50%)')
    True
    >>> check_web_color('hsl(0, 0%, 0%)')
    True
    >>> check_web_color('#fffaff')
    True
    >>> check_web_color('hsl(0, 25%, 70%)')
    True


    # Некорректные цвета
    >>> check_web_color('#2345')
    False
    >>> check_web_color('ffffff')
    False
    >>> check_web_color('rgb(257, 50, 10)')
    False
    >>> check_web_color('hsl(20, 10, 0.5)')
    False
    >>> check_web_color('hsl(34%, 20%, 50%)')
    False
    >>> check_web_color('hsl(-2, 25%, 60%)')
    False
    """
    pass



if __name__ == "__main__":
    doctest.testmod(verbose=True)
