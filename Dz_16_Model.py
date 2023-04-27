
import time
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as sqlalchemy_enum
from enum import Enum

class Base(DeclarativeBase):
    pass


engine = None
Session = sessionmaker()


def configure_engine():
    global engine
    if engine is None:
        engine = create_engine("postgresql://postgres:postgres@localhost:5432/Dz_16_Model")
        Session.configure(bind=engine)


class OperationName(Enum):
    PLUS = "Replenishment"
    MINUS = "Withdrawal"

class BankAcc(Base):
    __tablename__ = "bankacc"

    id_acc: Mapped[int] = mapped_column(primary_key=True)
    acc_name: Mapped[str]
    balance: Mapped[int]
    bankaccounthistory: Mapped["BankAccountHistory"] = relationship(back_populates="bankacc")


class BankAccountHistory(Base):
    __tablename__ = "bankaccounthistory"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_acc = mapped_column(ForeignKey("bankacc.id_acc"))
    bankacc: Mapped["BankAcc"] = relationship("BankAcc", back_populates="bankaccounthistory")
    amount: Mapped[int]
    date_time: Mapped[int]
    operation: Mapped[str] = mapped_column(sqlalchemy_enum(OperationName))

    def replenishment_of_the_balance(self, amount: int):
        self.amount = amount
        time.sleep(1)
        self.balance += self.amount
        self.history.append(BankAccountHistory(amount, OperationName.PLUS, datetime.now()))

    def withdrawals(self, amount: int):
        self.amount = amount
        time.sleep(1)
        self.balance -= self.amount
        self.history.append(BankAccountHistory(amount, OperationName.MINUS, datetime.now()))

configure_engine()
Base.metadata.create_all(engine)

session = Session()

account_Nick = BankAcc(acc_name="Nick", balance = 20)
session.add(account_Nick)
session.commit()

