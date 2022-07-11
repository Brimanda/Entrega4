from enum import Enum

class OrderStatus(Enum):

    CREATED = 'CREADA'
    PAYED = 'PAGADO'
    COMPLETED = 'COMPLETADO'
    CANCELED = 'CANCELADO'

choices = [ (tag, tag.value) for tag in OrderStatus]