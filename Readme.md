# AWS CLI Session Token Generator

This is a Python script that obtains temporary AWS credentials using the AWS Security Token Service (STS), sets them as environment variables for the AWS CLI to use, and prints out the export commands for these variables. The script prompts the user for their MFA token and serial number (or uses environment variables if available) to obtain the session token.

## Requirements

- Python 3.6 or higher
- \`boto3\` library
- AWS CLI (if you want to use the credentials with the CLI)

## Installation

1. Clone or download the repository:

   \`\`\`
   $ git clone https://github.com/nlauchande/aws-cli-session-token-generator.git
   \`\`\`

2. Install the required dependencies:

   \`\`\`
   $ pip install boto3
   \`\`\`

## Usage

1. Run the script:

   \`\`\`
   $ python session_token_generator.py
   \`\`\`

2. Follow the prompts to enter your MFA token and serial number.

3. The script will print out the export commands for the AWS CLI environment variables (\`AWS_ACCESS_KEY_ID\`, \`AWS_SECRET_ACCESS_KEY\`, and \`AWS_SESSION_TOKEN\`). Copy and paste these commands into your terminal to set the environment variables.

4. Use the AWS CLI with the temporary credentials:

   \`\`\`
   $ aws s3 ls
   \`\`\`

## Contributing

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   \`\`\`
   $ git checkout -b my-feature-branch
   \`\`\`

3. Make your changes and commit them:

   \`\`\`
   $ git commit -am 'Added a new feature'
   \`\`\`

4. Push your branch to GitHub:

   \`\`\`
   $ git push origin my-feature-branch
   \`\`\`

5. Create a pull request.

## License

This project is licensed under the MIT License. 

## Credits

This project was created by @nlauchande
