class MyMobile:
    def __init__(self, number):
        self.number = number
        self.switch = False
    def turn_on(self):
        self.switch = True
        return f'mobile phone {self.number} is enabled'
    def turn_off(self):
        self.switch = False
        return f'mobile phone {self.number} is off'
    def call(self, cally):
        self.cally = cally
        if self.switch: return f'number {self.number} calling {self.cally}'
        else: return f'mobile phone not working'

phone1 = MyMobile('+375291234567')
