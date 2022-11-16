from django import template

register = template.Library()

bad_word = ['привет','редиска',]
@register.filter()
def censor(value):
    text_split = value.lower().split()
    iter = -1
    for x in text_split:
        x = x.replace('.','').replace(',','')
        iter += 1
        if x in bad_word:
            for_len_x = (len(x) - 1) * '*'
            x = x.replace(x[1:], for_len_x)
            text_split[iter] = x
    return f'{" ".join(text_split)}'
