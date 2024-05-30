from worker import Worker,WorkerStatus
from order import Order
from order import Status

Couriers = []

class CourierTransport(Enum):
    FEET = 5
    BICYCLE = 15
    MONOWHEEL = 20
    ELECTRICSCOOTER = 25
    CAR = 50

class Courier(Worker):

    def give_order(self, order: Order):
        self.workerStatus = WorkerStatus.INPROGRESSWORK
        self.currentWork = order

    def take_order(self):
  
        self.currentWork.ChangeStatus(Status.ONTHEWAY)
        print(f'Доставляет заказ по адресу {self.currentWork.address}')
        self.giveOrder()

    def giveOrder(self):
        self.currentWork.status = Status.INPOINT
        self.workerStatus = WorkerStatus.FREE
        print(f'Курьер ДОставил заказ по адресу {self.currentWork.address}')
        self.currentWork = None 

