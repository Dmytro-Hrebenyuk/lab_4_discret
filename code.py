import random

class State:
    SLEEP = 0
    MORNING_ROUTINE = 1
    WORKING = 2
    EXERCISING = 3
    EATING = 4
    LEISURE_TIME = 5
    CRY = 6

class MyDayFSM:
    def __init__(self):
        self.state = State.SLEEP
        self.stopped = False

    def send(self, hour):
        if self.state == State.SLEEP:
            if random.random() > 0.9:
                print("Ah..., good new day")
                self.state = State.MORNING_ROUTINE
            elif random.random() > 0.9:
                print('lets eat')
            else:
                print("Zzzz...")
        elif self.state == State.MORNING_ROUTINE:
            if random.random() > 0.5:
                print("Lets work")
                self.state = State.WORKING
            else:
                print("Lets eat")
                self.state = State.EATING
        elif self.state == State.WORKING:
            if random.random() > 0.8:
                print("Break")
                self.state = State.LEISURE_TIME
            else:
                print("Working")
        elif self.state == State.EXERCISING:
            if random.random() > 0.5:
                print("Computer games")
                self.state = State.LEISURE_TIME
            elif random.random() > 0.5:
                print("Im tired")
                self.state = State.CRY
            else:
                print('Exersizing')
                self.state = State.EATING
        elif self.state == State.EATING:
            if random.random() > 0.5:
                print("Eating")
                self.state = State.WORKING
            else:
                print("Working")
                self.state = State.WORKING
        elif self.state == State.LEISURE_TIME:
            if random.random() > 0.5:
                print("Ah..., good")
                self.state = State.WORKING
            else:
                print("Eating")
                self.state = State.EATING
        elif self.state == State.CRY:
            if random.random() > 0.5:
                print("Crying")
                self.state = State.EATING
            else:
                print("Exersizing")
                self.state = State.EXERCISING

day_simulator = MyDayFSM()

for hour in range(24):
    print(f"Hour {hour + 1}:")
    day_simulator.send(hour)
