#Required libs for the code
import boto3
import logging
from creds import *
from machinespecs import *

#Enable logging
logging.basicConfig(level = logging.INFO, filename='ec2launchaccess.log', format='%(asctime)s:%(levelname)s,%(message)s')

#Getting required creds for both boto client and ec2 machine. We are fetching these details from file nameed creds.
ec2 = boto3.resource('ec2', aws_access_key_id=user_aws_access_key_id,
                     aws_secret_access_key=user_aws_secret_access_key,
                     region_name=user_region_name)

client = boto3.client('ec2', aws_access_key_id=user_aws_access_key_id,
                      aws_secret_access_key=user_aws_secret_access_key,
                      region_name=user_region_name)

#This code creates the ec2 instance and variables can be added here or also set as a input from an another file
instance=ec2.create_instances(
    ImageId='ami-0bdb1d6c15a40392c',
    MinCount=1,
    MaxCount=1,
    InstanceType=UserRequiredInstanceType,
    #NetworkInterfaces=[{'DeviceIndex':0}]
    NetworkInterfaces = [
        {
            'SubnetId': 'subnet-caec34ac',
            'DeviceIndex': 0,
            'AssociatePublicIpAddress': False,
            'Groups': ['sg-0818ad6c617d3fd0e','sg-948c83ee' ]
        }
    ]
)

#Getting the private IP from the response of the above
response = client.describe_instances(InstanceIds=[instance[0].id])['Reservations'][0]['Instances'][0]['PrivateIpAddress']
#print(response)
#Adding this IP information in the log
logging.info('Machine with Private IP {} is created'.format(response))


#Adding the file to ip files
file = open("ip.txt","w+")
file.write(response)
logging.info('Ip has been written to the IP file')
file.close()

