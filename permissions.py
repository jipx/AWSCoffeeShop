import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c72251a1453548l3913209t1w928410997426-s3bucket-7yjl3565xw9d"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")