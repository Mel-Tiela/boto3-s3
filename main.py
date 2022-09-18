import os.path

import boto3 as boto3
import botocore.exceptions
import logging

s3_client = boto3.client('s3', 'eu-central-1')


def upload_to_s3(file_path, bucket_name):
    try:
        file_name = os.path.basename(file_path)
        logger('INFO', 'Name of file: '.format(file_name))
        logger('INFO', 'File path : '.format(file_path))
        logger('INFO', 'Bucket Name: '.format(bucket_name))
        with open(file_path, 'rb') as file:
            s3_client.upload_fileobj(file, bucket_name, file_name)
    except botocore.exceptions.ClientError as error:
        logger('ERROR', error)


def create_s3_bucket():
    try:
        response = s3_client.create_bucket(Bucket='name-of-bucket',
                                           CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'})

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            logger('INFO', 'Bucket Created Successfully')
        else:
            logger('DEBUG', 'Bucket Not Created!!')
    except botocore.exceptions.ClientError as error:
        logger('ERROR', error)


def logger(log_level, msg):
    logging.basicConfig(filename='logs/s3_app.log', encoding='utf-8', level=logging.DEBUG,
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
    if log_level == 'ERROR':
        logging.error(msg)
    elif log_level == 'DEBUG':
        logging.debug(msg)
    elif log_level == 'INFO':
        logging.info(msg)
    elif log_level == 'WARNING':
        logging.warning(msg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_s3_bucket()
    upload_to_s3('path of file to upload',
                 'Name of the S3 bucket to uoload file')
