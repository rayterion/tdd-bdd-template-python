from core.account_loader import AccountLoader, Database
from unittest import TestCase

class TestAccountLoader(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = Database()
        cls.loader = AccountLoader(cls.db)

    def teardown(self):
        self.db.clearAll()

    def test_load_existing_account(self):
        account = {
            'id': 1,
            'name': 'Test Account'
        }
        self.db.add_account(account)
        loaded_account = self.loader.load(1)
        self.assertEqual(loaded_account, account)

    def test_load_nonexistent_account(self):
        loaded_account = self.loader.load(999)
        self.assertIsNone(loaded_account)