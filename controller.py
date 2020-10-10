from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, car, **kwargs):
        Controller.__init__(self, **kwargs)
        self.car = car

    def on_x_press(self):
        print("circle pressed")
        self.car.right()

    def on_x_release(self):
        print("circle released")
        self.car.stop()

    def on_triangle_press(self):
        print("square pressed")
        self.car.left()

    def on_triangle_release(self):
        print("square released")
        self.car.stop()

    def on_circle_press(self):
        print("triangle pressed")
        self.car.forward()

    def on_circle_release(self):
        print("triangle released")
        self.car.stop()

    def on_square_press(self):
        print("x pressed")
        self.car.backward()

    def on_square_release(self):
        print("x released")
        self.car.stop()

