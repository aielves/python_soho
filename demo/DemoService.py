from database.aop.JdbcServiceAop import InitService, Transactional
from database.mvc.Base import BaseService
from demo.DemoModel import YtfBank


@InitService
class DemoService(BaseService):

    @Transactional(True)
    def save(self):
        bank = YtfBank()
        bank.id = 11
        bank.userId = 1
        bank.bankname = "工商银行"
        self.simpleJdbc.save(bank)
        self.simpleJdbc.save(bank)

if __name__ == '__main__':
    service = DemoService()
    result = service.save()
    print("完成保存")
    print(result)