
# B_data_keyword = "depth"
# C_received_data_keyword = "position"
# C_sent_data_keyword = "coefficient"
# target1 = "program_B"
# target2 = "program_C"

class MasterSensor():
    def __init__(self,*args):    
        #self.client = Client(args)
        pass

    def work(self):
        while True:
            
            #depth = self.client.get_data(B_data_keyword, target1)
            #pos_dict = self.client.get_data(C_received_data_keyword)
            #coe_dict = self.process_data(depth,pos_dict)
            #self.client.send_data(C_sent_data_keyword,target2)
            
            pass
            

    def process_data(self,depth, pos_dict):
        return {"x_coe" : pos_dict["x_pos"]/depth,
        "y_coe" : pos_dict["y_pos"]/(depth**2),
        "z_coe" : pos_dict["z_pos"]/(depth**3)
        }

master = MasterSensor()
master.work()