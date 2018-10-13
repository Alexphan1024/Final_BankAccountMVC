from control.BT_controller import *

if __name__ == "__main__":
    controller = BTController()
    while True:
        controller.start()