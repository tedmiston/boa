from boa import snakecase

def test_camelcase():
    snake = snakecase('someEvent')
    assert snake == 'some_event'

def test_lowercase():
    snake = snakecase('someevent')
    assert snake == 'someevent'

def test_special_char():
    snake = snakecase('Some Event\'s')
    assert snake == 'some_events'

def test_capital_spaced():
    snake = snakecase('Info Window')
    assert snake == 'info_window'

def test_mixed():
    snake = snakecase('trait_ID')
    assert snake == 'trait_id'

def test_lower_first_letter():
    snake = snakecase('Add to Collection')
    assert snake == 'add_to_collection'

def test_underscored():
    snake = snakecase('context_ip')
    assert snake == 'context_ip'

def test_colons():
    snake = snakecase('analytics:byway')
    assert snake == 'analytics_byway'
