import RPi.GPIO as GPIO          
from time import sleep
from car import Car
from controller import MyController

def main():
    car  = Car(2,3,4,17,27,22)
    controller = MyController(interface="/dev/input/js0", car=car, connecting_using_ds4drv=False)
    controller.listen()
    
if __name__ == "__main__":
    main()