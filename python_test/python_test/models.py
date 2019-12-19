from django.db.models import Model, CharField, EmailField


# Insert models here
class Client(Model):
    name = CharField(max_length=32, unique=True)
    street_address = CharField(max_length=32)
    suburb = CharField(max_length=32)
    postcode = CharField(max_length=32)
    state = CharField(max_length=32)
    contact_name = CharField(max_length=32)
    email_address = EmailField('email_address', unique=True)
    phone_number = CharField(max_length=32)

    def __str__(self):
        return ", ".join(
            self.client_name,
            "\n",
            self.street_address,
            self.suburb,
            "\n",
            self.postcode,
            self.state,
            self.contact_name,
            self.email_address,
            self.phone_number
        )
