import boa

def test_camelcase():
    snake = boa.constrict('someEvent')
    assert snake == 'some_event'

def test_lowercase():
    snake = boa.constrict('someevent')
    assert snake == 'someevent'

def test_special_char():
    snake = boa.constrict('Some Event\'s')
    assert snake == 'some_events'

def test_capital_spaced():
    snake = boa.constrict('Info Window')
    assert snake == 'info_window'

def test_mixed():
    snake = boa.constrict('trait_ID')
    assert snake == 'trait_id'

def test_lower_first_letter():
    snake = boa.constrict('Add to Collection')
    assert snake == 'add_to_collection'

def test_underscored():
    snake = boa.constrict('context_ip')
    assert snake == 'context_ip'

def test_colons():
    snake = boa.constrict('analytics:byway')
    assert snake == 'analytics_byway'
