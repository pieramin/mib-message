from faker import Faker

from .dao_test import DaoTest


class TestMessageManager(DaoTest):
    faker = Faker()

    @classmethod
    def setUpClass(cls):
        super(TestMessageManager, cls).setUpClass()
        from tests.models.test_message import TestMessage
        cls.test_message = TestMessage
        from mib.dao import message_manager
        cls.message_manager = message_manager.MessageManager

    def test_crud(self):
        for _ in range(0, 10):
            message = self.test_message.generate_random_message()
            self.message_manager.create_message(message=message)
            message1 = self.message_manager.retrieve_by_id(message.id)
            self.test_message.assertMessageEquals(message1, message)
            self.message_manager.update_message(message=message)
            message1 = self.message_manager.retrieve_by_id(message.id)
            self.test_message.assertMessageEquals(message1, message)
            self.message_manager.delete_message(message=message)
