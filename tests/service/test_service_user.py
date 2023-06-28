import pytest

from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user(self):
        name1 = "Mari"
        job1 = "Eng"
        resultado_esperado = "Usuário adicionado"

        service = ServiceUser()
        resultado = service.add_user(name=name1, job=job1)

        assert resultado == resultado_esperado


    def test_add_user_name_none_job_none(self):
        name1 = None
        job1 = None
        resultado_esperado = "Usuário não adicionado"

        service = ServiceUser()
        resultado = service.add_user(name=name1, job=job1)

        assert resultado == resultado_esperado


    def test_add_user_name_none_job_str(self):
        name1 = None
        job1 = "Analyst"
        resultado_esperado = "Usuário não adicionado"

        service = ServiceUser()
        resultado = service.add_user(name=name1, job=job1)

        assert resultado == resultado_esperado


    def test_add_user_name_str_job_none(self):
        name1 = "Maria"
        job1 = None
        resultado_esperado = "Usuário não adicionado"

        service = ServiceUser()
        resultado = service.add_user(name=name1, job=job1)

        assert resultado == resultado_esperado


    def test_add_user_already_exists(self):
        name1 = "Mari"
        job1 = "Tester"
        resultado_esperado = "Nome adicionado já existe"

        service = ServiceUser()
        service.add_user(name=name1, job=job1)
        resultado = service.add_user(name=name1, job=job1)

        assert resultado == resultado_esperado


    def test_add_user_type_name_str_type_job_int(self):
        name1 = "Maria"
        job1 = 34
        resultado_esperado = "Usuário não adicionado"

        service = ServiceUser()
        resultado = service.add_user(name=name1, job=job1)

        assert resultado == resultado_esperado


    def test_add_user_type_name_int_type_job_str(self):
        name1 = 12
        job1 = "Analista"
        resultado_esperado = "Usuário não adicionado"

        service = ServiceUser()
        resultado = service.add_user(name=name1, job=job1)

        assert resultado == resultado_esperado


    def test_add_user_type_name_int_type_job_int(self):
        name1 = 12
        job1 = 43
        resultado_esperado = "Usuário não adicionado"

        service = ServiceUser()
        resultado = service.add_user(name=name1, job=job1)

        assert resultado == resultado_esperado


    def test_delete_user(self):
        name1 = "Mari"
        job1 = "Eng"
        resultado_esperado = "Usuário removido com sucesso"

        service = ServiceUser()
        service.add_user(name=name1, job=job1)
        resultado = service.delete_user(name=name1)

        assert resultado == resultado_esperado

    def test_delete_user_not_found(self):
        name1 = "Mari"
        job1 = "Eng"
        resultado_esperado = "Usuário não encontrado"

        service = ServiceUser()
        resultado = service.delete_user(name=name1)

        assert resultado == resultado_esperado


    def test_update_user(self):
        name1 = "Mari"
        job1 = "Engenheira"
        resultado_esperado = "Trabalho atualizado com sucesso"

        service = ServiceUser()
        service.add_user(name=name1, job=job1)
        resultado = service.update_user(name=name1, job=job1)

        assert resultado == resultado_esperado

    def test_update_user_not_found(self):
        name1 = "Mari"
        job1 = "Eng"
        resultado_esperado = "Usuário não encontrado"

        service = ServiceUser()
        resultado = service.update_user(name=name1, job=job1)

        assert resultado == resultado_esperado

    def test_get_user(self):
        name1 = "Mari"
        job1 = "Eng"
        resultado_esperado = "Eng"

        service = ServiceUser()
        service.add_user(name=name1, job=job1)
        resultado = service.get_user(name=name1)

        assert resultado == resultado_esperado

    def test_get_user_not_found(self):
        name1 = "Mari"
        job1 = "Eng"
        resultado_esperado = "Usuário não encontrado"

        service = ServiceUser()
        resultado = service.get_user(name=name1)

        assert resultado == resultado_esperado


    def test_check_user_exists_if_not_found(self):
        name1 = "Mari"
        job1 = "Eng"
        resultado_esperado = "Usuário não encontrado"

        service = ServiceUser()
        resultado = service.check_user_exists(name=name1)

        assert resultado == resultado_esperado

