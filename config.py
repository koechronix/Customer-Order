import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Secret key for securing session data
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')  # Default value for development

    # Database configuration (PostgreSQL example)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://chemor:password@localhost/customer_orders')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Africa's Talking API configuration
    AFRICASTALKING_API_KEY = os.getenv('AFRICASTALKING_API_KEY')  # Ensure to set in .env
    AFRICASTALKING_USERNAME = os.getenv('AFRICASTALKING_USERNAME')  # Ensure to set in .env

    # OpenID Connect configuration (Google as an example)
    OIDC_CLIENT_ID = os.getenv('OIDC_CLIENT_ID')  # Ensure to set in .env
    OIDC_CLIENT_SECRET = os.getenv('OIDC_CLIENT_SECRET')  # Ensure to set in .env
    OIDC_AUTHORIZATION_URL = os.getenv('OIDC_AUTHORIZATION_URL', 'https://accounts.google.com/o/oauth2/auth')
    OIDC_TOKEN_URL = os.getenv('OIDC_TOKEN_URL', 'https://oauth2.googleapis.com/token')
    OIDC_USERINFO_URL = os.getenv('OIDC_USERINFO_URL', 'https://openidconnect.googleapis.com/v1/userinfo')
