from twilio.rest import Client
client = Client(SID, Token)
client.message.create(to='+92311545641', _from='+1864867963', body='message')