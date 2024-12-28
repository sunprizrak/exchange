# from sqlalchemy import Column, Integer, String, Float, Enum, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import enum
#
# # Создаем базовый класс для моделей
# Base = declarative_base()
#
# # Перечисление для статусов заказа
# class OrderStatus(enum.Enum):
#     PENDING = "pending"   # Заказ создан, ожидает подтверждения
#     COMPLETED = "completed"  # Заказ выполнен
#     CANCELED = "canceled"  # Заказ отменен
#
# # Модель Order
# class Order(Base):
#     __tablename__ = 'orders'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     telegram_id = Column(Integer, nullable=False, index=True)  # Telegram ID пользователя
#     telegram_username = Column(String, nullable=True)  # Telegram username пользователя
#     coin_name = Column(String, nullable=False)  # Название криптовалюты
#     coin_price = Column(Float, nullable=False)  # Цена за единицу криптовалюты
#     coin_amount = Column(Float, nullable=False)  # Количество криптовалюты
#     total_price = Column(Float, nullable=False)  # Общая стоимость
#     status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)  # Статус заказа
#
#     def __repr__(self):
#         return (f"<Order(id={self.id}, telegram_id={self.telegram_id}, "
#                 f"telegram_username={self.telegram_username}, coin_name={self.coin_name}, "
#                 f"coin_price={self.coin_price}, coin_amount={self.coin_amount}, "
#                 f"total_price={self.total_price}, status={self.status.value})>")