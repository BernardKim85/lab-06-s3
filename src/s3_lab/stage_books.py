#!/usr/bin/env python3
"""Create an S3 bucket named practice-<USER> in us-east-1."""
import logging
import os

import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

# practice-<USER>: bucket names must be globally unique across all of AWS
bucket_name = f"practice-khs3z-2"#{os.environ.get('USER', 'unknown')}"
log.info(f"{bucket_name}")

try:
    s3 = boto3.client("s3", region_name="us-east-1")
    # us-east-1: omit LocationConstraint or create_bucket fails
    s3.create_bucket(Bucket=bucket_name)
    log.info(f"Created bucket: {bucket_name}")
except ClientError as e:
    log.error(f"Error creating bucket {bucket_name}: {e}")

local_file = "cloud.jpg"  # must exist in the current directory
key = "folder/in/bucket/cloud.jpg"

try:
    s3 = boto3.client("s3")
    with open(local_file, "rb") as f:
        s3.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=f,
            ContentType="image/jpeg",  # so browsers can display, not download
        )
    log.info(f"Uploaded {local_file} to s3://{bucket_name}/{key}")
except FileNotFoundError:
    log.error(f"Local file not found: {local_file}")
except ClientError as e:
    log.error(f"Error uploading object: {e}")

def parse_args():
    '''parsing arguments'''
    list_file = sys.argv[1]
    index_path = sys.argv[2]
    bucket = sys.argv[3]
    if len sys.argv[1:4] < 3:
        sys.exit(1)
    return (list_file, index_path, bucket)
def download_book(list_file, dest_dir):
    '''downloading book'''
    list_file
def create_bucket(bucket):
    '''creating a public bucket'''

def make_public(bucket):
    '''making the bucket public'''
    s3.put_public_access_block(
        Bucket=bucket,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": False,
            "IgnorePublicAcls": False,
            "BlockPublicPolicy": False,
            "RestrictPublicBuckets": False,
        },
    )
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::public-pzb4me/*"
            }
        ]
    }
    s3.put_bucket_policy(Bucket=bucket, Policy=json.dumps(policy))
def upload_files(bucket, file_paths):
    '''uploading files'''

def upload_index(bucket, index_path):
    '''uploading index path'''

def main():
    '''main function'''
    parse_args()
    download_book()
    create_bucket()
    make_public()
    upload_files()
    upload_index


if __name__ == "__main__":
    main()