# # Using automation to send WhatsApp messages repeatedly without manual oversight could violate WhatsApp's terms of service and potentially lead to your number being banned. It's important to use such scripts responsibly and with awareness of the rules and potential consequences. Continuous or excessive automated messaging can be flagged as spam by service providers.

# If you decide to proceed with automated messaging, you should ensure it is done with the consent of the recipients and in a manner that does not disrupt or annoy them. Regular monitoring and human oversight are essential to prevent abuse of the service and to maintain compliance with WhatsApp's policies.

# For any sort of automated messaging, especially if intended for a business or service, you should use the official channels provided by the platform, such as the WhatsApp Business API, which are designed for this purpose and include guidelines to prevent misuse.


import pywhatkit
import time
from datetime import datetime, timedelta

phone_number = 'number'
message = 'This is a test from vs code py project 101'
interval = 60    

while True:
    
    next_send_time = datetime.now() + timedelta(minutes=interval)
    time_hour = next_send_time.hour
    time_minute = next_send_time.minute

    
    pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute)

   
    time.sleep((interval * 60) + 20)
