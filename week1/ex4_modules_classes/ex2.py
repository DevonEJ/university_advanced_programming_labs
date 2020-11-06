
class Name():
    first_name = ""
    surname = ""
    title = ""
    other_names = []

    def __init__(self, first_name, surname, title, *args):
        self.first_name = first_name
        self.surname = surname
        self.title = title
        self.other_names = args


    def formal_name(self):
        if len(self.other_names) == 0:
            print(f"{self.title.capitalize()} {self.first_name[0].upper()}. {self.surname.capitalize()}")
        else:
            shortened_middle_names = [name[0].upper() + "." for name in self.other_names[0]]
            # Handle double-surnames
            surnames = self.surname.split(" ")
            capitalized_surnames = [surname.capitalize() for surname in surnames]
            print(f"{self.title.capitalize()} {self.first_name[0].upper()}. {' '.join(shortened_middle_names)} {' '.join(capitalized_surnames)}")
        

class Person(object):
    name = None

    def __init__(self, first_name, surname, title, other_names, address, age):
        self.name = Name(first_name, surname, title, other_names)
        self.address = address
        self.age = age

    def personalDetails(self):
        return self.name, self.address, self.age


class Tutor(Person):
    id = 0
    def __init__(self, first_name, surname, title, other_names, address, age, salary, id):
        super(Tutor, self).__init__(first_name, surname, title, other_names, address, age)
        self.salary = salary
        self.id = id
    def personalDetails(self):
        return super(Tutor, self).personalDetails(), 
        self.salary, self.id 
               

class Student(Person):
    def __init__(self, first_name, surname, title, other_names, address, age, id):
        super(Student, self).__init__(first_name, surname, title, other_names, address, age)
        self.id = id

    def personalDetails(self):
        return super(Student, self).personalDetails(),self.id
   


# name = Name("devon", "edwards joseph", "Miss", ["amy", "elliot"])
# name.formal_name()

student = Student("devon", "edwards joseph", "miss", ["amy"], "London", 28, "454545")
student.name.formal_name()
