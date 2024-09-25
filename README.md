## Customer Order API
A simple API to manage customers and their orders, integrated with Africa's Talking for SMS notifications and OpenID Connect for authentication.

## Table of Contents
- Documentation
- Installation
- Usage
- Configuration
- Authentication
- SMS Notifications
- Testing
- Deployment
  -Deploying to AWS EC2
- Contributing
- License
- Documentation
- Refer to the API docs here.

Installation
To install the required dependencies, run:
 ```bash 
  pip install -r requirements.txt
  ```

Usage
Initialize the application:
1.Clone the repository:
```bash
git clone https://github.com/koechronix/Customer-Order
cd Customer_Order_API
```
Set up environment variables:

2.Create a .env file in the root directory and add your credentials:
```bash
SECRET_KEY=your_secret_key
AT_API_KEY=your_africas_talking_api_key
AT_USERNAME=sandbox
OIDC_CLIENT_ID=your_oidc_client_id
OIDC_CLIENT_SECRET=your_oidc_client_secret
DATABASE_URL=postgresql://test_user:password@localhost/customer_orders
```
3.Run the application:
```bash
flask run
```
Configuration
Make sure your config.py file is set up to load from your .env file:
```bash 
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Africa's Talking API configuration
    AFRICASTALKING_API_KEY = os.getenv('AT_API_KEY')
    AFRICASTALKING_USERNAME = os.getenv('AT_USERNAME')

    # OpenID Connect configuration
    OIDC_CLIENT_ID = os.getenv('OIDC_CLIENT_ID')
    OIDC_CLIENT_SECRET = os.getenv('OIDC_CLIENT_SECRET')
    OIDC_AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/auth'
    OIDC_TOKEN_URL = 'https://oauth2.googleapis.com/token'
    OIDC_USERINFO_URL = 'https://openidconnect.googleapis.com/v1/userinfo'
```
## Authentication
The application uses OpenID Connect for user authentication. To log in, visit the /login endpoint.

## SMS Notifications
The application sends SMS notifications for new orders using Africa's Talking. Ensure you have valid credentials in your .env file to send SMS.

## Testing
To run tests with coverage checking, execute the following command:
```bash
pytest --cov=app tests/
```
### NEXT STEPS(OPTIONAL)
## Deployment
- Deploying to AWS EC2
- Follow these steps to deploy your application to an AWS EC2 instance:

1.Create an EC2 Instance:

-Log in to your AWS Management Console.
-Navigate to EC2 and launch a new instance (choose an Ubuntu server).
-Connect to Your Instance:

 - Use SSH to connect to your instance:
 ```bash 
 Deployment
Deploying to AWS EC2
Follow these steps to deploy your application to an AWS EC2 instance:

Create an EC2 Instance:

Log in to your AWS Management Console.
Navigate to EC2 and launch a new instance (choose an Ubuntu server).
Connect to Your Instance:

Use SSH to connect to your instance:
```
3.Install Dependencies:

- Update the package list and install required packages:
```bash 
sudo apt update
sudo apt install python3-pip python3-venv postgresql postgresql-contrib
```
4.Clone Your Repository:
```bash 
git clone https://github.com/koechronix/Customer-Order
cd Customer_Order_API
```
5.Set Up a Virtual Environment:
```bash 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
6.Configure the Database:

-Set up PostgreSQL and create the database:
```bash 
sudo -u postgres psql
CREATE DATABASE customer_orders;
CREATE USER test_user WITH PASSWORD 'password';
ALTER ROLE test_user SET client_encoding TO 'utf8';
ALTER ROLE test_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE test_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE customer_orders TO test_user;
\q
```
7.Run Migrations:

- If you're using Flask-Migrate, run:
```bash
flask db upgrade
```
8.Start the Application:
```bash 
flask run --host=0.0.0.0
```
9.Access the Application:

Open your browser and navigate to http://your-ec2-public-ip:5000.
## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your changes.

## License
This project is licensed under the MIT Licence
