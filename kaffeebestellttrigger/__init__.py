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
        conn_str="<connection_string>")
    table_name = "CoffeemachineDataTable"
    table_client = table_service_client.create_table(table_name=table_name)

    my_data_json = msg.get_body().decode('utf-8')
    my_data_string = json.loads(my_data_json)

    Coffeemachine_ID = my_data_string.split(",")[0]
    Coffee_name = my_data_string.split(",")[1]

    my_entity = {
        u'PartitionKey': Coffeemachine_ID,
        u'RowKey': Coffee_name
    }

    table_service_client = TableServiceClient.from_connection_string(
        conn_str="<connection_string>")
    table_client = table_service_client.get_table_client(table_name=table_name)

    entity = table_client.create_entity(entity=my_entity)
