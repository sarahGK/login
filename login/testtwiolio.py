from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException

client = TwilioRestClient(account='AC8cdba7c0b7a032d1bc17e13f02bd1b31',
                          token='4d60f1e68a313b9ce43866cb40253d3b')
try:
response = client.caller_ids.get('+1234567890')
except TwilioRestException as e:
  if e.code == 20404:
    print("The phone number does not exist.")
  else:
    raise e

print(response.validation_code)


