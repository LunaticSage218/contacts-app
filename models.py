class Contact:
    def __init__(self, id=None, name="", phone="", address=""):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "address": self.address
        }
