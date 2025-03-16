import mobile_phone_class as mpc


def test_turn_on_true():
    mpc.phone1.turn_on()
    assert mpc.phone1.switch == True


def test_turn_off_false():
    mpc.phone1.turn_off()
    assert mpc.phone1.switch == False


def test_turn_call_true():
    mpc.phone1.turn_on()
    mpc.phone1.call('911')
    assert mpc.phone1.switch == True


def test_turn_call_false():
    mpc.phone1.turn_off()
    mpc.phone1.call('911')
    assert mpc.phone1.switch == False
