import logging
import json
import azure.functions as func
from azure.data.tables import TableServiceClient
from datetime import datetime


def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))

    connection_string = "HostName=iot3bhwii22-dz.azure-devices.net;DeviceId=Notebook-dz;SharedAccessKey=cGXDrnQ85YU9fNj1zog8r7Q7Da6avBAlqpsz0gnaFBs="
    table_service_client = TableServiceClient.from_connection_string(
        conn_str="DefaultEndpointsProtocol=https;AccountName=coffeemachinedata;AccountKey=LHaBP5X84VzuZ3bieHiLjv5y3x9cSJAPic6K0qGxpZ2YkKuPUtahoh1fiLf1GWzxdA6n5n+2AJVB4cCUOGGzzw==;EndpointSuffix=core.windows.net")
    table_name = "coffemachineTable"

    my_data_json = msg.get_body().decode('utf-8')
    my_data_string = json.loads(my_data_json)

    Coffeemachine_ID = my_data_string.split(",")[0]
    Coffee_name = my_data_string.split(",")[1]

    my_entity = {
        u'PartitionKey': Coffeemachine_ID,
        u'RowKey': Coffee_name
    }

    table_client = table_service_client.get_table_client(table_name=table_name)

    entity = table_client.create_entity(entity=my_entity)
