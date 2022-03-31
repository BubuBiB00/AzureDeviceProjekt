from azure.iot.device import IoTHubDeviceClient 
from random import randrange


connection_string = "HostName=iot3bhwii22-dz.azure-devices.net;DeviceId=Notebook-dz;SharedAccessKey=cGXDrnQ85YU9fNj1zog8r7Q7Da6avBAlqpsz0gnaFBs=" 
client = IoTHubDeviceClient.create_from_connection_string(connection_string)


def coffeemachines():
    coffeemachine_id = [0,1,2,3,4]
    coffeemachine_coffee = ["Schwarz","Capuccino","Grosser Brauner","Kleiner Brauner","Verlaengerter"]
    coffeemachine_coffee_num = 0

    coffeemachine_msg = [coffeemachine_id[randrange(0,len(coffeemachine_id))],coffeemachine_coffee[randrange(0,len(coffeemachine_coffee))],coffeemachine_coffee_num]

    return coffeemachine_msg


def main(): 

    try: 
        msg = coffeemachines()
        print(msg)

    except KeyboardInterrupt: 
        print("Stopped!")
        

if __name__ == '__main__':
    main()