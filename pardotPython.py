# Python wrapper for Pardot to create users, could be useful to replace PHP integration
from pypardot.client import PardotAPI
from dotenv import load_dotenv

load_dotenv()

pardotAuth = PardotAPI(
    email='PARDOT_EMAIL',
    password='PARDOT_PASSWORD',
    user_key='PARDOT_KEY'
)

pardotAuth.authenticate()

# Creating a new prospect
pardotAuth.create(email='dante1498@gmail.com', first_name='Ethan', last_name='Gough')

# Read data about our prospect
print(pardotAuth.prospects.read_by_email(email='dante1498@gmail.com'))
