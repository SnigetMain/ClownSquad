from datetime import datetime, date, time
from client import Client, Clients, add_client
from cart import Cart
from cooker import Cooker
from courier import Courier
from facility import Facilities, add_facility, Facility
from order import Order, Status
from payment import Payment

client = Clients[0]

def command_pack():
    client.choose_facility()
    # client.choose_product()