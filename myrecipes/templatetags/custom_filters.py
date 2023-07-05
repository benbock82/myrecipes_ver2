import re
from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()


@register.filter
def youtube_id(value):
    """
    Extracts the YouTube video ID from the given URL.
    """
    query = urlparse(value)
    if query.hostname == 'www.youtube.com' or query.hostname == 'youtube.com':
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
    if query.hostname == 'youtu.be':
        return query.path[1:]
    # Return an empty string if the URL is not recognized as a YouTube video
    return ''


@register.filter
def replace_email_characters(email):
    username, _ = email.split('@')
    return f"{username}@{'*' * 8}"



