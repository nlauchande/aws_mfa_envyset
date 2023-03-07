import boto3
import os
import sys

def get_mfa_token():
    """Prompts the user for their MFA token."""
    mfa_token = input("Enter your MFA token: ")
    return mfa_token

def get_aws_session_token(mfa_serial):
    """Gets an AWS session token using the provided MFA serial number."""
    sts_client = boto3.client("sts")
    response = sts_client.get_session_token(
        DurationSeconds=3600,
        SerialNumber=mfa_serial,
        TokenCode=input("Enter your MFA token: ")
    )
    return response["Credentials"]

def main():
    """Main function that reads the MFA serial number from an environment variable, gets an AWS session token using the provided MFA serial number and MFA token (if available), and sets environment variables for the AWS CLI to use."""
    mfa_serial = os.getenv("AWS_MFA_SERIAL")

    if mfa_serial is not None:
        # Use the MFA serial number from the environment variable
        credentials = get_aws_session_token(mfa_serial)
    else:
        # Prompt the user for their MFA token and serial number
        mfa_serial = input("Enter your MFA serial number: ")
        mfa_token = get_mfa_token()
        credentials = get_aws_session_token(mfa_serial)

    # Set environment variables for the AWS CLI to use
    os.environ["AWS_ACCESS_KEY_ID"] = credentials["AccessKeyId"]
    os.environ["AWS_SECRET_ACCESS_KEY"] = credentials["SecretAccessKey"]
    os.environ["AWS_SESSION_TOKEN"] = credentials["SessionToken"]

    # Run the AWS CLI command
    print("export "+"AWS_ACCESS_KEY_ID="+os.environ['AWS_ACCESS_KEY_ID'] + "\n")
    print("export "+"AWS_SECRET_ACCESS_KEY="+os.environ['AWS_SECRET_ACCESS_KEY'] + "\n")
    print("export "+"AWS_SESSION_TOKEN="+os.environ['AWS_SESSION_TOKEN']+ "\n")


if __name__ == "__main__":
    main()
