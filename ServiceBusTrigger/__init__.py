import logging
import json
import uuid
#from azure.data.tables import TableServiceClient
from datetime import datetime
import azure.functions as func

def main(msg: func.ServiceBusMessage):
    logging.info('Python queue trigger function processed a queue item.')
    message = msg.get_body().decode('utf-8')
    
    logging.info(message)
    # such das: create entity in azure tables with python

    
    #result = json.dumps({
    #    u'PartitionKey': Kaffemachine,
    #    u'RowKey': PRODUCT_ID,
    #    'message_id': msg.message_id,
    #    'body': msg.get_body().decode('utf-8'),
    #    'content_type': msg.content_type,
    #    'expiration_time': msg.expiration_time,
    #    'label': msg.label,
    #    'partition_key': msg.partition_key,
    #    'reply_to': msg.reply_to,
    #    'reply_to_session_id': msg.reply_to_session_id,
    #    'scheduled_enqueue_time': msg.scheduled_enqueue_time,
    #    'session_id': msg.session_id,
    #    'time_to_live': msg.time_to_live,
    #    'to': msg.to,
    #    'user_properties': msg.user_properties,
    #    'metadata' : msg.metadata
    #}, default=str)

    # my_entity = {
    #     u'PartitionKey': 1234,
    #     u'RowKey': 1,
    #     u'Coffeemachine': 15,
    #     u'Price': 9.99,
    #     u'Comments': u"great product",
    #     u'OnSale': True,
    #     u'ReducedPrice': 7.99,
    #     u'PurchaseDate': datetime(1973, 10, 4),
    #     u'BinaryRepresentation': b'product_name'
    #     }


    # table_service_client = TableServiceClient.from_connection_string(conn_str="<connection_string>")
    # table_client = table_service_client.get_table_client(table_name="myTable")

    # entity = table_client.create_entity(entity=my_entity)