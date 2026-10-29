from abc import ABC, abstractmethod

'''
Deine Aufgabe

1. Schreibe einen EmailAdapter. Er braucht einen Betreff, den dein Interface nicht kennt. Lege dafür einfach einen festen Text fest, z. B. "Benachrichtigung".
2. Schreibe einen SmsAdapter. Das SDK will keine einzelnen Parameter, sondern ein Dictionary mit den Schlüsseln number und content.
3. Baue Alarm einmal mit dem E-Mail-Adapter und einmal mit dem SMS-Adapter zusammen und rufe jeweils trigger(...) auf. Als Empfänger nimmst du 
   "anna@example.com" bzw. "0171 1234567".
'''

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient, text):
        ...

# Dein Code: kennt nur den Standard
class Alarm:
    def __init__(self, notifier):
        self.notifier = notifier

    def trigger(self, recipient):
        self.notifier.send(recipient, "Achtung: Server ist down!")



# Fremder Code: darfst du nicht ändern
class EmailSDK:
    def send_mail(self, to_address, subject, body):
        print(f"E-Mail an {to_address} | Betreff: {subject} | {body}")

class SmsSDK:
    def send_sms(self, message_data):
        print(f"SMS an {message_data['number']}: {message_data['content']}")


class EmailAdapter(Notifier):
    def __init__(self):
        self.e_send = EmailSDK()
    
    def send(self, recipient, text):
        self.e_send.send_mail(recipient,"Benachrichtigung", text)

alarm = Alarm(EmailAdapter())
alarm.trigger("anna@gmail.com")