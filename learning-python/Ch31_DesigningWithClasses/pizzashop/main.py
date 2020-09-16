from employee import Employee, PizzaRobot, Chef, Server
from shop import Shop

if __name__ == "__main__":
    bob = PizzaRobot("bob")
    bob.work()
    print(bob)
    bob.give_raise(0.1)
    print(bob)

    for c in Employee, Chef, Server, PizzaRobot:
        obj = c(c.__name__)
        obj.work()

    print("======================")

    scene = Shop()
    scene.order("Anne")
    print("...")
    scene.order("Ellie")