from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):

        if name is None or job is None:
            return "Usuário não adicionado"

        user = self.check_user_exists(name)

        if name != None and job != None:
            #if type(name) == str:
                if type(name) == str and type(job) == str:
                    if name is not None and job is not None:
                        user = User(name=name, job=job)
                        self.store.bd.append(user)
                    return "Usuário adicionado"

                return "Usuário não adicionado"

        if name == user.name:
            return "Nome adicionado já existe"

    def delete_user(self, name):
        user = self.check_user_exists(name)

        if type(user) == str:
            return user
        else:
            self.store.bd.remove(user)
            return "Usuário removido com sucesso"

    def update_user(self, name, job):

        user = self.check_user_exists(name)

        if type(user) == str:
            return user

        else:
            index = self.store.bd.index(user)
            user.job = job
            self.store.bd[index] = user

            return "Trabalho atualizado com sucesso"

    def get_user(self, name):

        user = self.check_user_exists(name)

        if type(user) == str:
            return user

        if user.name == name:
            return user.job

    def check_user_exists(self, name):

        for user in self.store.bd:
            if user.name == name:
                return user

        return "Usuário não encontrado"

