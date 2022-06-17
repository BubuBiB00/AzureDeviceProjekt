import logging
import json
import azure.functions as func
from azure.data.tables import TableServiceClient
from datetime import datetime


def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))

    connection_string = "DefaultEndpointsProtocol=https;AccountName=coffeemachinedata;AccountKey=LHaBP5X84VzuZ3bieHiLjv5y3x9cSJAPic6K0qGxpZ2YkKuPUtahoh1fiLf1GWzxdA6n5n+2AJVB4cCUOGGzzw==;EndpointSuffix=core.windows.net"
    table_service_client = TableServiceClient.from_connection_string(
        conn_str=connection_string)
    table_name = "coffemachineTable"
    table_client = table_service_client.create_table(table_name=table_name)

    device_id = msg.metadata(["UserProperties"]["iothub-connection-device-id"])
    
    my_data_json = msg.get_body().decode('utf-8')
    bestellung = json.loads(my_data_json)
    
    machine = str(bestellung["CMachineID"])
    sorte = str(bestellung["CSorte"])

    my_entity = {
        u'PartitionKey': str(device_id),
        u'RowKey': str(datetime.now().isoformat()),
        u'Machine ID': machine,
        u'Sorte' : sorte

    }

    table_service_client = TableServiceClient.from_connection_string(
        conn_str=connection_string)
    table_client = table_service_client.get_table_client(table_name=table_name)

    entity = table_client.create_entity(entity=my_entity)
