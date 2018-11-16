class Car(object):
    def __init__(hi, name):
        hi.miles = 0
        hi.name = name

    def speak(hi, text):
        print(hi.name, 'says', text)

car1 = Car('kitt')
car1.speak('hey')
