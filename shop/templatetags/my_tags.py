from django import template

register = template.Library()

@register.filter()
def media_filter(path):
    if path:
        return f'/media/{path}'
    return '#'

@register.filter()
def price_filter(price):
    try:
        # Преобразуем цену в строку с разделителями тысяч
        return f'{int(price):,}'.replace(',', ' ')
    except (ValueError, TypeError):
        # Если цена не является числом, вернем её без изменений
        return price

@register.filter()
def mouse_filter(object):
    pass
    # if object.category == 'Мышки':