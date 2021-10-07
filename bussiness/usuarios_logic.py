from Base_de_datos.dataUsuarios import UsuarioData
from entities.models import Users
from typing import List, Optional, Union


class UserLogic:
    def __init__(self):
        self.datasource = UsuarioData()

    def get(self, usr: str) -> Optional[Users]:
        """:return: User-->Exists|| None-->Not found"""
        u = self.datasource.GetOne(usr)
        return u

    def all(self) -> List[Users]:
        us = self.datasource.GetAll()
        return us

    def login(self, user: str, password: str) -> Union[Users, bool, None]:
        """:return: User -> password is ok,
          False -> password is wrong,
          None -> User not found"""
        u = self.get(user)
        if u is None:
            print("user not found")
            return None
        if u.check_password(password):
            print("contraseña correcta")
            return u
        print("contraseña incorrecta")
        return False

    def update(self, user) -> bool:
        """:returns: if saved changes
        :remember check password here"""
        return self.datasource.update(user)

    def register(self, user) -> bool:
        print("registro***")
        return self.datasource.register(user)
