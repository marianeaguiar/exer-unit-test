from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

store = Store()
#print(store.bd)

name1 = "Mari"
job1 = "Analyst"

user = User(name=name1, job=job1)
#print(user.name)
#print(user.job)

print("#Primeiro teste")
name1 = "Mari"
job1 = "Analyst"

service = ServiceUser()
resultado = service.add_user(name=name1, job=job1)
print(service.store.bd[0].name)
print(service.store.bd[0].job)
print(resultado)


print("#Segundo teste")
name1 = None
job1 = "Analyst"

service = ServiceUser()
resultado = service.add_user(name=name1, job=job1)
print(service.store.bd)
print(resultado)


print("#Terceiro teste")
name1 = "Mari"
job1 = "Analyst"

service = ServiceUser()
resultado = service.add_user(name=name1, job=job1)
print(service.store.bd[0].name)
print(service.store.bd[0].job)
print(resultado)





