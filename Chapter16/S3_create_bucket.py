#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import boto3

s3_resource = boto3.resource("s3")

bucket = s3_resource.create_bucket(Bucket="my_first_bucket", CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})
print(bucket)
