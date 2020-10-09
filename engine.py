import RPi.GPIO as GPIO          
from time import sleep
from car import Car

def main():
    car  = Car(2,3,4,17,27,22)
    while(True):
        x = raw_input()
        if x == 'f':
            car.forward()
        elif x == 'b':
            car.backward()
        elif x == 'r':
            car.right()
        elif x == 'l':
            car.left()
        elif x == 's':
            car.stop()
        elif x == 'u':
            car.gearUp()
        elif x == 'd':
            car.gearDown()
        else:
            break

if __name__ == "__main__":
    main()