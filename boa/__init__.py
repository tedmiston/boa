"""
Convert strings to snakecase.
"""

import re

spaces_re = re.compile(r'\s+')
strip_re = re.compile(r'[^\w]+')
first_cap_re = re.compile(r'(.)([A-Z][a-z]+)')
all_cap_re = re.compile(r'([a-z0-9])([A-Z])')
dedupe_re = re.compile(r'\_+')

def constrict(string):
    """Convert the input string to snakecase + lowercase."""

    # Whitespace to underscores
    output = spaces_re.sub('_', string)

    # Strip non-alphanumeric/underscore chars
    output = strip_re.sub('', output)

    # Snake case
    output = first_cap_re.sub(r'\1_\2', output)
    output = all_cap_re.sub(r'\1_\2', output).lower()

    # Remove multiple sequential underscores
    output = dedupe_re.sub('_', output)

    return output
