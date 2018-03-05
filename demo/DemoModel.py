from database.mvc.Base import IDEntity


class TestUser(IDEntity):
    def __init__(self):
        super(TestUser, self).__init__()
        self.username = None
        self.nickname = None
        self.mobile = None
        self.ctime = None

    def getTableName(self):
        return "user"


class YtfBank(IDEntity):
    def __init__(self):
        super(YtfBank, self).__init__()
        self.userId = None
        self.bankname = None
        self.ctime = None

    def getTableName(self):
        return "ytf_bank"


if __name__ == "__main__":
    my = TestUser();
    print(my.getTableName())
    print(my.__dict__)
