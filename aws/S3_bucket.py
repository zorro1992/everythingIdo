#!/usr/bin/python
import boto3
from boto3.session import Session
s3 = boto3.setup_default_session(region_name='us-west-2')
session = Session(aws_access_key_id='AKIAJUJE2U4ES67MISGQ',aws_secret_access_key='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')

s3 = session.resource('s3')
s3.create_bucket(Bucket='myfbucket789076541253334')
