import boto3
import os

def off_instance(event, context):

    ec2 = boto3.resource('ec2', region_name=os.environ['region'])

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name',
                  'Values': ['running']}])

    for instance in instances:
        instance.stop()
        print('Stopped instance: ', instance.id)

def on_instance(event, context):

    ec2 = boto3.resource('ec2', region_name=os.environ['region'])

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name',
                  'Values': ['stopped']}])

    for instance in instances:
        instance.start()
        print('Started instance: ', instance.id)