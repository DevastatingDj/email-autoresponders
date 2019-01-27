# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC357f2add95e5f12f2eb45892b491f01c'
auth_token = 'a5185656672701fae3186b7ad2282ab5'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+17753129791',
                              body='\n APKO MILI HAI CHUDAI K LIYE EK CHUUT FREE "/\" \n AAP BAS PAYTM KARE RS. 2000 ISS NUMBER PAR - 8130393405',
                              to='+917289877320'
                          )

print(message.sid)