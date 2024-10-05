import boto3
from botocore.exceptions import ClientError
import logging
logging.basicConfig(level=logging.DEBUG)

DYNAMODB = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")

class DynamoDBFacade:
    def __init__(self) -> None:
        pass

    def create_category_table(self, table_name):
        try:
            table = DYNAMODB.create_table(
                TableName = table_name,
                KeySchema = [
                    {
                        'AttributeName' : 'category',
                        'KeyType' : 'HASH'
                    },
                    {
                        'AttributeName' : 'prompt_id',
                        'KeyType' : 'RANGE'
                    }
                ],
                AttributeDefinitions = [
                    {
                        'AttributeName' : 'category',
                        'AttributeType' : 'S'
                    },
                    {
                        'AttributeName' : 'prompt_id',
                        'AttributeType' : 'N'
                    }
                ],
                ProvisionedThroughput = {
                    'ReadCapacityUnits': 100,
                    'WriteCapacityUnits': 100 
                }
            )
            logging.info("Table created successfully!")
            return table
        except ClientError as e:
            logging.error(f"Unable to create table: {e}")

    def add_prompt(self, table_name, category, prompt_id, prompt):
        table = DYNAMODB.Table(table_name)
        
        try:
            response = table.put_item(
                Item={
                    "category" : category,
                    "prompt_id" : prompt_id,
                    "prompt" : prompt
                }
            )
            
            logging.info("Prompt added successfully!")
        except ClientError as e:
            logging.error(f"Unable to upload prompt: {e}")
        
    
    def get_prompt(self, table_name, category, prompt_id):
        table = DYNAMODB.Table(table_name)

        try:
            response = table.get_item(
                Key={
                    "category": category,
                    "prompt_id": prompt_id
                }
            )

            logging.info("Prompt retrieved successfully!")
            return response['Item']['prompt']
        except ClientError as e:
            logging.error(f"Unable to get prompt: {e}")

    def delete_table(self, table_name):
        table = DYNAMODB.Table(table_name)

        try:
            table.delete()
            logging.info("Table deleted successfully")
        except ClientError as e:
            logging.error(f"Unable to delete table: {e}")
