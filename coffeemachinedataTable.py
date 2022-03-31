from azure.data.tables import TableServiceClient
from azure.data.tables import TableEntity
from azure.core.credentials import AzureNamedKeyCredential


credential = AzureNamedKeyCredential("myaccount", "mykey")
table_service = TableServiceClient(endpoint="mytableendpoint", credential=credential)
table_service = TableServiceClient.from_connection_string(conn_str='DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;TableEndpoint=mytableendpoint;')
table_service.create_table('coffemachineTable')
