import hashlib
import datetime
import json

# كلاس العملة
class SamiCoin:
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.chain = []
        self.current_transactions = []

        # إنشاء كتلة التكوين الأولى (Genesis block)
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # إفراغ قائمة المعاملات الحالية
        self.current_transactions = []

        # إضافة الكتلة الجديدة لسلسلة الكتل
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # تحويل الكتلة إلى نص
        block_string = json.dumps(block, sort_keys=True).encode()
        # حساب الهاش باستخدام خوارزمية SHA-256
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

# إنشاء العملة
samicoin = SamiCoin('SamiCoin', 'SAM', 500000000)

# تجربة إنشاء عملية المعاملة الأولى
samicoin.new_transaction('John', 'Sam', 10)

# تجربة إنشاء كتلة جديدة
samicoin.new_block(12345)

# طباعة سلسلة الكتل
print(samicoin.chain)