from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def give_raise(self, percent):
        self.pay *= 1 + percent


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, "manger", pay)

    def give_raise(self, percent, bonus=.1):
        # super() it's not a preferable Pythonic way of using inheritance, there could be issues with multi inheritance
        # so you should use explicit parent class instead
        # super(Manager, self).give_raise(percent + bonus)
        Person.give_raise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raises(self):
        for member in self.members:
            member.give_raise(.1)

    def show_all(self):
        for member in self.members:
            print(member)


if __name__ == "__main__":
    bob = Person("Bob")
    sue = Person("Sue", "dev", 10000)
    andy = Person("Andy", job="volunteer")
    drake_list = ["drake", 100000]
    drake = Manager(*drake_list)
    ann_dist = {"name": "Ann", "pay": 1000}
    ann = Person(**ann_dist)

    persons = [bob, sue, andy, drake, ann]

    for person in persons:
        print(person)

    sue.give_raise(.10)
    print(sue)
    drake.give_raise(.10)
    print(drake)

    print("\n===== DEPARTMENT =====")
    department = Department(bob, andy, drake)
    department.give_raises()
    department.show_all()
