import main


def test_no_letters():
    assert main.howmanyletters('') == 'no data'


def test_less_that_3_Letters():
    assert main.howmanyletters('NO') == 'less than three letters!'


def test_more_than_or_3_letters():
    assert main.howmanyletters('lol :)') == ['lol', ':)']
