import uuid

from aiohttp import web
from app.api.models import InfoAboutDevice, Users
import jwt
from jwt.exceptions import DecodeError


SECRET = 'a708c84a366141e5a97c16d9bb5e372a'


class ListDeviceView(web.View):

    async def get(self):
        try:
            token = self.request.headers.get('Authorization').encode()
        except AttributeError:
            error = 'Authorization not found'
            return web.json_response({'error': error})
        check = await self._protected_handler(token)
        if check:
            devices = await InfoAboutDevice.query.order_by(InfoAboutDevice.id).gino.all()
            devices_data = []
            for device in devices:
                devices_data.append({
                    "id": device.id,
                    "devicetype": device.devicetype,
                    "manufacture": device.manufacture,
                    "model": device.model,
                    "storage": device.storage,
                    "price": [
                        device.grade_a,
                        device.grade_b,
                        device.grade_c,
                        device.grade_d,
                    ]

                })
            return web.json_response(data={'messages': devices_data})
        else:
            return web.json_response(data={'Error': 'Something is wrong with the token'})

    @staticmethod
    async def _protected_handler(token):
        try:
            token = token.decode('utf8').replace('Bearer ', '')
            jwt.decode(token, SECRET)
            return True
        except (TypeError, DecodeError) as exc:
            return web.json_response({'error': f'{exc}'})


class GetLoginAndPassword(web.View):

    async def get(self):
        login = uuid.uuid4().hex
        password = uuid.uuid4().hex
        user = await self.request.app["db"].users.create(
            login=login,
            password=password,
        )
        return web.json_response(
            data={
                'user': {
                    'login': user.login,
                    'password': user.password
                }
            }
        )


class GetJsonWebToken(web.View):

    async def post(self):
        data = await self.request.json()

        log = data.get('login')
        password = data.get('password')

        try:
            if await self._check_user(log, password):
                token = await self._get_token(log)
                return web.json_response({'access_token': token})
            else:
                return web.json_response({'error': 'password or username do not match'})

        except AttributeError:
            return web.json_response({'error': 'password or username do not match'})

    @staticmethod
    async def _check_user(log, passw):

        login_password = await Users.query.where(Users.login == log).gino.first()
        login_password = login_password.to_dict()
        user, pword = login_password['login'], login_password['password']

        return True if log == user and passw == pword else False

    @staticmethod
    async def _get_token(log):
        return jwt.encode({"login": f'{log}', "scopes": [f"create_by: project"]}, SECRET).decode('utf8')
