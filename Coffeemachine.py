from azure.iot.device import IoTHubDeviceClient
from random import randrange
import json

CONNECTION_STRING = "HostName=iot3bhwii22-dz.azure-devices.net;DeviceId=Notebook-dz;SharedAccessKey=cGXDrnQ85YU9fNj1zog8r7Q7Da6avBAlqpsz0gnaFBs=" 
DEVICE_ID = "Notebook-dz"
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def coffeemachines():
    global coffeemachine_coffee_num

    coffeemachine_id = [0,1,2,3,4]
    coffeemachine_coffee = ["Schwarz","Capuccino","Grosser Brauner","Kleiner Brauner","Verlaengerter"]
    coffeemachine_coffee_num = 0

    coffeemachine_msg = ""+str(coffeemachine_id[randrange(0,len(coffeemachine_id))])+str(coffeemachine_coffee[randrange(0,len(coffeemachine_coffee))])+str(coffeemachine_coffee_num)


    coffemachine_json = json.dumps(coffeemachine_msg)

    print(coffemachine_json)
    return coffemachine_json
    


def main(): 
    global coffeemachine_coffee_num

    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    client.connect()
    
    coffeemachine_data = coffeemachines()

    client.send_message(coffeemachine_data)
    client.disconnect()
    client.shutdown()
    print("successfully sent")
        
if __name__ == '__main__':
    main()