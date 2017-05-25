import re

title_re = re.compile('(^|\s)(\S)')
underscore_re = re.compile('[:]+')
strip_re = re.compile('[^\w]+')
first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')
dedupe_re = re.compile('\_+')

def snakecase(string):
    # Title case before removing spaces, to preserve words
    capped = title_re.sub(lambda m: m.group(1) + m.group(2).upper(), string)

    # Replace some chars with underscores
    # XXX: Roadtrippers hack/fix
    underscored = underscore_re.sub('_', capped)

    # Strip non-alphanumeric/underscore chars
    stripped = strip_re.sub('', underscored)

    # Snake case
    snake1 = first_cap_re.sub(r'\1_\2', stripped)
    snake2 = all_cap_re.sub(r'\1_\2', snake1).lower()

    # Remove multiple sequential underscores
    deduped = dedupe_re.sub('_', snake2)
    return deduped
