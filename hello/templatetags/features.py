from django import template
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta

import markdown2

register = template.Library()

@register.filter(name='duration_filter')
def duration_filter(value):

    time = timedelta(seconds=int(value))
    date = datetime(1, 1, 1) + time

    return "%d:%d:%d:%d" % (date.day-1, date.hour, date.minute, date.second)

@register.filter(name='markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML '''   
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)

@register.filter(name='convert_seconds')
def convert_seconds(seconds):
    seconds = int(seconds)
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return "%dd %dh %dm %ds" % (days, hours, minutes, seconds)
