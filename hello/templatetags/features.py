from django import template

from datetime import datetime, timedelta

register = template.Library()

@register.filter(name='duration_filter')
def duration_filter(value):

    time = timedelta(seconds=int(value))
    date = datetime(1, 1, 1) + time

    return "%d:%d:%d:%d" % (date.day-1, date.hour, date.minute, date.second)
