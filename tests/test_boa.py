from nose2.tools import params

import boa

def test_null():
    output = boa.constrict(None)
    assert output == ''

def test_blank():
    output = boa.constrict('')
    assert output == ''

def test_lowercase():
    output = boa.constrict('someevent')
    assert output == 'someevent'

def test_uppercase():
    output = boa.constrict('SOMEEVENT')
    assert output == 'someevent'

def test_capitalized():
    output = boa.constrict('Someevent')
    assert output == 'someevent'

@params(
    ('SomeEvent',),
    ('someEvent',),
)
def test_camelcased(string):
    output = boa.constrict(string)
    assert output == 'some_event'

@params(
    ('Some "Events"',),
    ('Some Event\'s',),
)
def test_special_chars(string):
    output = boa.constrict(string)
    assert output == 'some_events'

@params(
    ('INFO WINDOW',),
    ('Info Window',),
    ('info Window',),
    ('Info window',),
    ('info window',),
)
def test_spaced(string):
    output = boa.constrict(string)
    assert output == 'info_window'

@params(
    ('trait_ID'),
    ('Trait_ID'),
    ('Trait_id'),
)
def test_mixed(string):
    output = boa.constrict(string)
    assert output == 'trait_id'

def test_lower_first_letter():
    output = boa.constrict('Add to Collection')
    assert output == 'add_to_collection'

def test_underscored():
    output = boa.constrict('context_ip')
    assert output == 'context_ip'
