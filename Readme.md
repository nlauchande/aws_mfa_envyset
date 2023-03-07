# AWS CLI Session Token Generator

This is a Python script that obtains temporary AWS credentials using the AWS Security Token Service (STS), sets them as environment variables for the AWS CLI to use, and prints out the export commands for these variables. The script prompts the user for their MFA token and serial number (or uses environment variables if available) to obtain the session token.

## Requirements

- Python 3.6 or higher
- `boto3` library
- AWS CLI (if you want to use the credentials with the CLI)

## Installation

1. Clone or download the repository:

