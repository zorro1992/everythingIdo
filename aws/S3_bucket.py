#!/usr/bin/python
import boto3
from boto3.session import Session
session = Session(aws_access_key_id='xvz',aws_secret_access_key='xyz',region_name='us-east-1')

s3 = session.resource('s3')
s3.create_bucket(Bucket='everythingidos3')
