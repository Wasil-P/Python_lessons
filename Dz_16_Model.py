
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


engine = None
Session = sessionmaker()


def configure_engine():
    global engine
    if engine is None:
        engine = create_engine("postgresql://postgres:postgres@localhost:5432/Dz_16_Model")
        Session.configure(bind=engine)


class OperationName(Base):
    __tablename__ = "operationname"

    id_operation: Mapped[int] = mapped_column(primary_key=True)
    operation_name: Mapped[str]
    bankaccounthistory: Mapped["BankAccountHistory"] = relationship(back_populates="operationname")


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
    id_operation = mapped_column(ForeignKey("operationname.id_operation"))
    operationname: Mapped["OperationName"] = relationship("OperationName", back_populates="bankaccounthistory")


configure_engine()
Base.metadata.create_all(engine)

session = Session()

account_Nick = BankAcc(acc_name="Nick", balance = 20)
session.add(account_Nick)
session.commit()

operationname_plus = OperationName(operation_name="PLUS")
session.add(operationname_plus)
session.commit()

operationname_minus = OperationName(operation_name="MINUS")
session.add(operationname_minus)
session.commit()