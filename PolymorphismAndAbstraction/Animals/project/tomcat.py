from project.cat import Cat

from project.dog import Dog


class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        super().__init__(name, age, gender)


    @staticmethod
    def make_sound():
        return "Hiss"


