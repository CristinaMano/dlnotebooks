
import boto3
import sagemaker
print(boto3.__version__)
sagemaker = boto3.client('sagemaker')
dir(sagemaker)