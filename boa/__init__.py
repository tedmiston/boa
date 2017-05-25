import re

title_re = re.compile('(^|\s)(\S)')
strip_re = re.compile(r'[^\w]+')
first_cap_re = re.compile(r'(.)([A-Z][a-z]+)')
all_cap_re = re.compile(r'([a-z0-9])([A-Z])')
dedupe_re = re.compile(r'\_+')

def constrict(string):
    # Title case before removing spaces, to preserve words
    output = title_re.sub(lambda m: m.group(1) + m.group(2).upper(), string)

    # Strip non-alphanumeric/underscore chars
    output = strip_re.sub('', output)

    # Snake case
    output = first_cap_re.sub(r'\1_\2', output)
    output = all_cap_re.sub(r'\1_\2', output).lower()

    # Remove multiple sequential underscores
    output = dedupe_re.sub('_', output)

    return output
