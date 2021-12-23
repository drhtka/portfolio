# -*- coding: utf-8 -*-
from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()

@register.filter(is_safe = False)
@stringfilter
def rupluralize(value, forms):
    """
    Подбирает окончание существительному после числа
    {{someval|pluralize:"товар,товара,товаров"}}
    """
    try:
        one, two, many = forms.split(u',')
        value = str(value)[-2:]  # 314 -> 14

        if (21 > int(value) > 4):
            return many

        if value.endswith('1'):
            return one
        elif value.endswith(('2', '3', '4')):
            return two
        else:
            return many

    except (ValueError, TypeError):
        return ''


# # Стандартный импорт библиотеки шаблонов
# from django import template
#
# # Это чтобы register.filter работал
# register = template.Library()
#
# # Расскажем django о нашем крутом фильтре
# @register.filter
# def rupluralize(value, arg="дурак,дурака,дураков"):
#     args = arg.split(",")
#     number = abs(int(value))
#     a = number % 10
#     b = number % 100
#
#     if (a == 1) and (b != 11):
#         return args[0]
#     elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
#         return args[1]
#     else:
#         return args[2]