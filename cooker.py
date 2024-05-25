from worker import Worker, WorkerStatus
from order import Order,Status
from Provaider import Provider

class Cooker(Worker):

    def give_order(self, order: Order):
        self.workerStatus = WorkerStatus.INPROGRESSWORK
        self.currentWork = order

    def order_assembly(self, order: Order,provider:Provider):
        print(f'Работает над заказом ID: {order.orderId}')
        self.package(provider)
        

    def package(self,provider:Provider):
        self.currentWork.ChangeStatus(Status.INSTOCK)
        for item in self.currentWork.itemList:
            provider.warehouse[item]-= 1
        self.currentWork = None
        print("Упаковал заказ")
        self.workerStatus = WorkerStatus.FREE
        
