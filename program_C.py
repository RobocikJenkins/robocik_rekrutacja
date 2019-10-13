from random import randint

# sent_data_keyword = "position"
# received_data_keyword = "coefficient"
# data_target = "program_A"

class PositionSensor():
    x_coe = 0
    y_coe = 0
    z_coe = 0

    def __init__(self):
        pass

    def get_position(self):
        x_pos = (randint(100,200)/100) * self.x_coe
        y_pos = (randint(200,300)/100) * self.y_coe
        z_pos = (randint(300,400)/100) * self.z_coe
        pos_dict = {
            "x" : x_pos,
            "y" : y_pos,
            "z" : z_pos
        }
        return pos_dict

    def extract_coe(self,received_dict):
        try:
            self.x_coe = received_dict["x_coe"]
            self.y_coe = received_dict["y_coe"]
            self.z_coe = received_dict["z_coe"]
        except KeyError:
            print("Received dict not valid")




if __name__ == "__main__":
    sensor = PositionSensor()
    #client = Client(*args)
    while True:
        data = sensor.get_position()
        
        #client.send_data(data_keyword,data,target)
        #received_dict = client.get_data(data_keyword,target)
        
        #sensor.extract_coe({"x_coe" : 10,"y_coe" : 20, "z_coe" : 30})