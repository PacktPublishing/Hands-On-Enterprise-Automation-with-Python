#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import boto3

s3_resource = boto3.resource("s3")
bucket = s3_resource.Bucket("my_first_bucket")

with open('~/test_file.txt', 'rb') as uploaded_data:
    bucket.put_object(Body=uploaded_data)
