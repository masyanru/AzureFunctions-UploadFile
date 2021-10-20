import logging
import azure.functions as func
import os
from azure.storage.blob import BlobServiceClient, BlobClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        file = req.files.get('file')
        logging.info(file.filename)
        
        connect_str=os.environ["AzureWebJobsStorage"]
        container='samples-workitems'
        
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client =blob_service_client.get_blob_client(container=container,blob=file.filename)
        blob_client.upload_blob(file)
    except Exception as ex:
        logging.info(ex.args)
       
    return func.HttpResponse("ok")