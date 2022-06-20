from azure.iot.device import IoTHubDeviceClient
from random import randint
from Kaffeemachinendaten import KaffeeMaschineKlasse
import json

CONNECTION_STRING = "HostName=iot3bhwii22-dz.azure-devices.net;DeviceId=Notebook-dz;SharedAccessKey=cGXDrnQ85YU9fNj1zog8r7Q7Da6avBAlqpsz0gnaFBs="
DEVICE_ID = "Notebook-dz"
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)


def coffeemachines():
    coffeemachine_id = [0, 1, 2, 3, 4]
    coffeemachine_coffee = ["Schwarz", "Capuccino",
                            "Grosser Brauner", "Kleiner Brauner", "Verlaengerter"]
    KaffeeMaschine = KaffeeMaschineKlasse(
        coffeemachine_id[randint(0, 4)], coffeemachine_coffee[randint(0, 4)])
    print(KaffeeMaschine.CMachineID, KaffeeMaschine.CSorte)
    kaffee_daten_json = json.dumps(KaffeeMaschine.__dict__)

    return kaffee_daten_json


def main():
    client = IoTHubDeviceClient.create_from_connection_string(
        CONNECTION_STRING)
    client.connect()

    coffeemachine_data = coffeemachines()

    client.send_message(coffeemachine_data)
    client.disconnect()
    client.shutdown()
    print("successfully sent")


if __name__ == '__main__':
    main()
