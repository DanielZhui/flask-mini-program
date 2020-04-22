import math
import datetime
from flask import g, render_template


def iPagination(params):
    ret = {
        "is_prev":1,
        "is_next":1,
        "from" :0 ,
        "end":0,
        "current":0,
        "total_pages":0,
        "page_size" : 0,
        "total" : 0,
        "url":params['url']
    }

    total = int(params['total'])
    page_size = int(params['page_size'])
    page = int(params['page'])
    display = int(params['display'])
    total_pages = int(math.ceil(total / page_size))
    total_pages = total_pages if total_pages > 0 else 1

    if page <= 1:
        ret['is_next'] = 0
    # 这里？？？
    if page >= total_pages:
        ret['is_next'] = 0

    display_median = int(math.ceil(display / 2))

    if page - display_median > 0:
        ret['from'] = page - display_median
    
    if page - display_median < 0:
        ret['from'] = 1

    if page + display_median <= total_pages:
        ret['end'] = page + display_median
    else:
        ret['end'] = total_pages

    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range(ret['from'], ret['end'] + 1)
    return ret

'''
统一渲染的方法
'''
def ops_render(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)

def getCurrentDate():
    return datetime.datetime.now()