# 218. Encapsulation in Object-Oriented Programming (OOP)

# Encapsulation :data hiding + controlled access.
class Student:
    def __init__(self, name):
        self.__name = name   # private attribute

    def get_name(self):     
        return self.__name

    def set_name(self, name): 
        self.__name = name

s = Student("Ujjwal")
print(s.get_name())  


# more ex using Email 
class Email:
    def __init__(self, sender, recipient, subject, body):
        # Private attributes (encapsulated data)
        self.__sender = sender
        self.__recipient = recipient
        self.__subject = subject
        self.__body = body

    # Getter methods
    def get_sender(self):
        return self.__sender

    def get_recipient(self):
        return self.__recipient

    def get_subject(self):
        return self.__subject

    def get_body(self):
        return self.__body

    # Setter methods
    def set_subject(self, subject):
        self.__subject = subject

    def set_body(self, body):
        self.__body = body

    # Public interface methods
    def send_email(self):
        # Logic related to sending email
        print(f" Sending email to {self.__recipient}...")

    def read_email(self):
        # Safe way to access encapsulated data
        return {
            "from": self.__sender,
            "to": self.__recipient,
            "subject": self.__subject,
            "body": self.__body,
        }


# Example usage
email = Email("ujjwal@gmail.com", "me@gmail.com", "Hello", "How are you?")
# Access via method
print(email.read_email())          
# Modify via setter
email.set_subject("Updated Hello") 
print(email.get_subject())
