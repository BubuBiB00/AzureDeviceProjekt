from azure.iot.device import IoTHubDeviceClient
from azure.iot.hub import IoTHubRegistryManager
from random import randrange


CONNECTION_STRING = "HostName=iot3bhwii22-dz.azure-devices.net;DeviceId=Notebook-dz;SharedAccessKey=cGXDrnQ85YU9fNj1zog8r7Q7Da6avBAlqpsz0gnaFBs=" 
DEVICE_ID = "Notebook-dz"
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def coffeemachines():
    global coffeemachine_coffee_num

    coffeemachine_id = [0,1,2,3,4]
    coffeemachine_coffee = ["Schwarz","Capuccino","Grosser Brauner","Kleiner Brauner","Verlaengerter"]
    coffeemachine_coffee_num = 0

    coffeemachine_msg = [coffeemachine_id[randrange(0,len(coffeemachine_id))],coffeemachine_coffee[randrange(0,len(coffeemachine_coffee))],coffeemachine_coffee_num]

    return coffeemachine_msg


def main(): 
    global coffeemachine_coffee_num

    try: 
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING)

        data = coffeemachines()
        if coffeemachine_coffee_num == 50:
            coffeemachine_coffee_num = 0
            
        registry_manager.send_c2d_message(DEVICE_ID, data)

    except KeyboardInterrupt: 
        print("Stopped!")
        
if __name__ == '__main__':
    main()