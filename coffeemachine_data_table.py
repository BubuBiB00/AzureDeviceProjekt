from azure.data.tables import TableServiceClient
from azure.data.tables import TableEntity
from azure.core.credentials import AzureNamedKeyCredential


connection_string = "DefaultEndpointsProtocol=https;AccountName=coffeemachinedata;AccountKey=LHaBP5X84VzuZ3bieHiLjv5y3x9cSJAPic6K0qGxpZ2YkKuPUtahoh1fiLf1GWzxdA6n5n+2AJVB4cCUOGGzzw==;EndpointSuffix=core.windows.net"

#credential = AzureNamedKeyCredential("coffeemachinedata", "mykey") #mykey
#table_service = TableServiceClient(endpoint="mytableendpoint", credential=credential) #mytableendpoint
table_service = TableServiceClient.from_connection_string(conn_str=connection_string) #table_service.create_table('coffemachineTable')

table_client = table_service.get_table_client(table_name="coffemachineTable")
coffemachine = {u'PartitionKey': u'id', u'RowKey': u'001', u'coffetype' : u'milliliters'}
table_client.create_entity(entity=coffemachine)

coffemachine = TableEntity()
table_client.create_entity(coffemachine)

coffemachine = {u'PartitionKey': u'id', u'RowKey': u'001', u'coffetype' : u'milliliters'}
table_client.update_entity(entity=coffemachine)