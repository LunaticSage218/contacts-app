import json
from service import ContactService

class ContactController:

    def __init__(self):
        self.service = ContactService()

    def get_contacts(self):
        contacts = self.service.list_contacts()
        return json.dumps([c.to_dict() for c in contacts]).encode()

    def create_contact(self, body):
        data = json.loads(body)
        self.service.create_contact(data)

    def update_contact(self, contact_id, body):
        data = json.loads(body)
        self.service.modify_contact(contact_id, data)

    def delete_contact(self, contact_id):
        self.service.remove_contact(contact_id)
