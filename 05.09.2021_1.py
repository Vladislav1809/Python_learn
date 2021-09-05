from time import sleep


class TrafficLight:
    def __init__(self):
        self.__color = {'Red': 3, 'Yellow': 1, 'Green': 2}

    def running(self):
        for color, time in self.__color.items():
            print(color, f"wait for {time} seconds")
            sleep(time)


traffic_light = TrafficLight()
traffic_light.running()
