from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Boolean,
    Text,
    Enum
)

from utils.model_base import Base


class UsersModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), unique=True, index=True, nullable=False)
    name = Column(String(50), index=True, nullable=False)
    mobile = Column(String(15), index=True, unique=True)
    profile = Column(String(255), nullable=False)
    is_verified = Column(Boolean, default=False)
    password = Column(String(128), nullable=False)
    verified_at = Column(DateTime())
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow)


class RolesModel(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow)


class UserRoleModel(Base):
    __tablename__ = 'user_role'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UsersModel.id), primary_key=True, nullable=False)
    roles_id = Column(Integer, ForeignKey(RolesModel.id), primary_key=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow)


class UserAddressModel(Base):
    __tablename__ = 'users_address'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UsersModel.id), primary_key=True, nullable=False)
    roles_id = Column(Integer, ForeignKey(RolesModel.id), primary_key=True, nullable=False)

    state = Column(String(150), nullable=False)
    city = Column(String(150), nullable=False)
    country = Column(String(100), nullable=False)
    zip_code = Column(String(6), nullable=False)
    address_1 = Column(Text, nullable=False)
    address_2 = Column(Text)
    landmark = Column(String(200))
    is_default = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    address_type = Column(Enum('Home', 'Office', 'Other'))
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow)
