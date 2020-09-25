from os import environ
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')


def my_handler(event, context):
    logger.info('In hello world lambda!')

    message = 'Hello from Lambda3!'
    table_name = environ['DDB_TABLE']
    log_stream_name = context.log_stream_name

    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key={'id': log_stream_name},
        UpdateExpression='set invocations = if_not_exists(invocations, :start) + :inc',
        ExpressionAttributeValues={
            ':start': 0,
            ':inc': 1
        },
        ReturnValues='ALL_NEW'
    )
    logger.info('Dynamo call completed with response:', response)

    logger.info('returning message:', message)
    return {'body': message}
