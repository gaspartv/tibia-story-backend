from rest_framework.test import APITestCase
from rest_framework.views import status
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


User: AbstractUser = get_user_model()


class UserLoginViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.BASE_URL = "/api/user/login/"
        cls.maxDiff = None

    def test_user_login_without_required_fields(self):
        response = self.client.post(self.BASE_URL, data={}, format="json")

        with self.subTest():
            expected_status_code = status.HTTP_400_BAD_REQUEST
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST sem todos os campos obrigatórios "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        returned_data: dict = response.json()
        expected_fields = {
            "username",
            "password",
        }
        returned_fields = set(returned_data.keys())
        msg = "Verifique se todas as chaves obrigatórias são retornadas ao tentar logar um usuário sem dados"
        self.assertSetEqual(expected_fields, returned_fields, msg)

    def test_login_success(self):
        register_data = {
            "username": "test_username",
            "email": "test_email@mail.com",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "password": "test_password",
        }
        User.objects.create_user(**register_data)
        login_data = {
            "username": "test_username",
            "password": "test_password",
        }

        with self.subTest():
            response = self.client.post(self.BASE_URL, data=login_data, format="json")
            expected_status_code = status.HTTP_200_OK
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        expected_keys = {"access", "refresh"}
        returned_keys = set(response.json().keys())
        msg = (
            "Verifique se o token está sendo retornado corretamente "
            + f"em `{self.BASE_URL}`"
        )

        self.assertSetEqual(expected_keys, returned_keys, msg)

    def test_login_with_wrong_credentials(self):
        login_data = {
            "username": "test_username_credentials_error",
            "password": "test_password_credentials_error",
        }

        # STATUS CODE
        with self.subTest():
            response = self.client.post(self.BASE_URL, data=login_data, format="json")
            expected_status_code = status.HTTP_401_UNAUTHORIZED
            returned_status_code = response.status_code
            msg = (
                "Verifique se o status code retornado do POST "
                + f"em `{self.BASE_URL}` é {expected_status_code}"
            )
            self.assertEqual(expected_status_code, returned_status_code, msg)

        # RETORNO JSON
        returned_data: dict = response.json()
        expected_data = {"detail": "No active account found with the given credentials"}
        msg = "Verifique se a mensagem de credenciais inválidas está correta"
        self.assertDictEqual(expected_data, returned_data, msg)
