def zodiac_sign(day, month):
    """
    >>> zodiac_sign(21, 3)
    'Овен'

    >>> zodiac_sign(20, 4)
    'Овен'

    >>> zodiac_sign(21, 4)
    'Телец'

    >>> zodiac_sign(20, 5)
    'Телец'

    >>> zodiac_sign(21, 5)
    'Близнецы'

    >>> zodiac_sign(21, 6)
    'Близнецы'

    >>> zodiac_sign(22, 6)
    'Рак'

    >>> zodiac_sign(22, 7)
    'Рак'

    >>> zodiac_sign(23, 7)
    'Лев'

    >>> zodiac_sign(23, 8)
    'Лев'

    >>> zodiac_sign(24, 8)
    'Дева'

    >>> zodiac_sign(23, 9)
    'Дева'

    >>> zodiac_sign(24, 9)
    'Весы'

    >>> zodiac_sign(23,10)
    'Весы'

    >>> zodiac_sign(24,10)
    'Скорпион'

    >>> zodiac_sign(22,11)
    'Скорпион'

    >>> zodiac_sign(23,11)
    'Стрелец'

    >>> zodiac_sign(21,12)
    'Стрелец'

    >>> zodiac_sign(22,12)
    'Козерог'

    >>> zodiac_sign(20,1)
    'Козерог'

    >>> zodiac_sign(21,1)
    'Водолей'

    >>> zodiac_sign(20,2)
    'Водолей'

    >>> zodiac_sign(21,2)
    'Рыбы'

    >>> zodiac_sign(20,3)
    'Рыбы'

    >>> zodiac_sign(0,111)
    ''
    """

    signs = [
        [21,3,'Овен',20,4],
        [21,4,'Телец',20,5],
        [21,5,'Близнецы',21,6],
        [22,6,'Рак',22,7],
        [23,7,'Лев',23,8],
        [24,8,'Дева',23,9],
        [24,9,'Весы',23,10],
        [24,10,'Скорпион',22,11],
        [23,11,'Стрелец',21,12],
        [22,12,'Козерог',20,1],
        [21,1,'Водолей',20,2],
        [21,2,'Рыбы',20,3]
    ]

    for sign in signs:
        if (month == sign[1] and day >= sign[0]) or (month == sign[4] and day <= sign[3]):
            return sign[2]

    return ''
