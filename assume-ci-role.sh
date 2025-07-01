#!/bin/bash
# Using bash instead of zsh for better compatibility in CI environments

# Exit gracefully if profile doesn't exist
_assume_role="arn:aws:iam::370957321024:role/GitHub-CI-MPL-Dafny-Role-us-west-2"
_session_name="OurCIAccount"
export AWS_REGION=us-west-2

# Check if the AWS profile exists
if aws configure list-profiles 2>/dev/null | grep -q "aws-crypto-tools-team+optools-ci-ToolsDevelopment"; then
  echo "Found required AWS profile, attempting to assume role..."
  STS_RESPONSE=$(AWS_PROFILE=aws-crypto-tools-team+optools-ci-ToolsDevelopment aws sts assume-role --role-arn $_assume_role --role-session-name $_session_name)
  
  # Only set credentials if the assume role was successful
  if [ $? -eq 0 ]; then
    export AWS_ACCESS_KEY_ID=$(echo "$STS_RESPONSE" | jq -r .Credentials.AccessKeyId)
    export AWS_SECRET_ACCESS_KEY=$(echo "$STS_RESPONSE" | jq -r .Credentials.SecretAccessKey)
    export AWS_SESSION_TOKEN=$(echo "$STS_RESPONSE" | jq -r .Credentials.SessionToken)
    echo "Successfully assumed CI role"
    unset AWS_PROFILE AWS_SDK_LOAD_CONFIG
  else
    echo "Failed to assume role"
  fi
else
  echo "AWS profile 'aws-crypto-tools-team+optools-ci-ToolsDevelopment' not found."
  echo "KMS tests that require AWS credentials will be skipped."
fi

unset _assume_role _session_name
