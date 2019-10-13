from random import randint

# data_keyword = "depth"
# data_pytarget = "program_A"

class DepthSensor():
    def __init__(self):
        pass
    def get_depth(self):
        return randint(1,100)


if __name__ == "__main__":
    sensor = DepthSensor()
    #client = Client(*args)
    while True:
        
        data = sensor.get_depth()
        #client.send_data(data_keyword,data,target)