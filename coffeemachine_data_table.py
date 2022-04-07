from azure.data.tables import TableServiceClient
from azure.data.tables import TableEntity
from azure.core.credentials import AzureNamedKeyCredential


credential = AzureNamedKeyCredential("coffeemachinedata", "mykey")
table_service = TableServiceClient(endpoint="mytableendpoint", credential=credential)
table_service = TableServiceClient.from_connection_string(conn_str='DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;TableEndpoint=mytableendpoint;')
table_service.create_table('coffemachineTable')

table_client = table_service.get_table_client(table_name="coffemachineTable")
coffemachine = {u'PartitionKey': u'id', u'RowKey': u'001', u'coffetype' : u'milliliters'}
table_client.create_entity(entity=coffemachine)

coffemachine = TableEntity()
table_client.create_entity(coffemachine)

coffemachine = {u'PartitionKey': u'id', u'RowKey': u'001', u'coffetype' : u'milliliters'}
table_client.update_entity(entity=coffemachine)