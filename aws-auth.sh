#!/bin/zsh

# AWS authentication script to assume role
_assume_role="arn:aws:iam::370957321024:role/GitHub-CI-MPL-Dafny-Role-us-west-2"
_session_name="OurCIAccount"
export AWS_REGION=us-west-2

echo "Authenticating with AWS using role assumption..."

STS_RESPONSE=`AWS_PROFILE=aws-crypto-tools-team+optools-ci-ToolsDevelopment aws sts assume-role --role-arn $_assume_role --role-session-name $_session_name`

if [ $? -eq 0 ]; then
    export AWS_ACCESS_KEY_ID=`echo "$STS_RESPONSE" | jq -r .Credentials.AccessKeyId`
    export AWS_SECRET_ACCESS_KEY=`echo "$STS_RESPONSE" | jq -r .Credentials.SecretAccessKey`
    export AWS_SESSION_TOKEN=`echo "$STS_RESPONSE" | jq -r .Credentials.SessionToken`
    unset AWS_PROFILE AWS_SDK_LOAD_CONFIG _assume_role _session_name
    
    echo "AWS authentication successful. Environment variables set."
else
    echo "AWS authentication failed. Please check your AWS configuration and try again."
    return 1
fi
