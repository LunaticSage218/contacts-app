from models import Contact
from database import ContactRepository

class ContactService:

    def __init__(self):
        self.repo = ContactRepository()

    def list_contacts(self):
        return self.repo.get_all()

    def create_contact(self, data):
        contact = Contact(
            name=data["name"],
            phone=data["phone"],
            address=data["address"]
        )
        self.repo.add(contact)

    def modify_contact(self, contact_id, data):
        contact = Contact(
            id=contact_id,
            name=data["name"],
            phone=data["phone"],
            address=data["address"]
        )
        self.repo.update(contact)

    def remove_contact(self, contact_id):
        self.repo.delete(contact_id)
