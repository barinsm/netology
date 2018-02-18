# Домашнее задание к лекции 1.7 «Классы и их применение в Python»
# Необходимо реализовать классы животных на ферме:
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

class Animal(object):
    tail = 1
    eyes = 2 
    def eat(self):
        return 'Ест: '
    def scream(self):
        return 'Кричит: '

class Ungulate(Animal):
    legs = 4
    hooves = 4
    fur = True
    ears = 2

class Bird(Animal):
    legs = 2
    wings = 2
    feathers = True
    beak = 1

class Cow(Ungulate):
    name = 'Корова'
    horns = 2
    def scream(self):
        return super(Cow, self).scream()+'Мууу'

class Goat(Ungulate):
    name = 'Коза'
    horns = 2
    def scream(self):
        return super(Cow, self).scream()+'Меее'

class Sheep(Ungulate):
    name = 'Овца'
    def scream(self):
        return super(Cow, self).scream()+'Беее'
        
class Pig(Ungulate):
    name = 'Свинья'
    snout = 1 
    def scream(self):
        return super(Cow, self).scream()+'Хрю-хрю-хрю'

class Duck(Bird):
    name = 'Утка'
    def scream(self):
        return super(Cow, self).scream()+'Кря-кря-кря'

class Hen(Bird):
    name = 'Курица'
    def scream(self):
        return super(Cow, self).scream()+'Ко-ко-ко'

class Goose(Bird):
    name = 'Гусь'
    def scream(self):
        return super(Cow, self).scream()+'Га-га-га'


a = Cow()

print(a.name, 'Ног:', a.legs, a.scream())
