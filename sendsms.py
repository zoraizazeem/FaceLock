
from twilio.rest import Client
def sendmess():
    client = Client("account_sid", "auth_token")
    
    client.messages.create(to="+447931793113", 
                           from_="your twilio no.", 
                           body="Hi Zoraiz, You recently tried to access your passwords! Was this you?")
                           
