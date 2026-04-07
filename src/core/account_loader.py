
class Database:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account['id']] = account

    def find_by_id(self, account_id):
        return self.accounts.get(account_id)

    def clearAll(self):
        self.accounts.clear()

class AccountLoader:
    def __init__(self, db):
        self.db = db

    def load(self, account_id):
        return self.db.find_by_id(account_id)