from app.api.views import ListDeviceView, GetLoginAndPassword, GetJsonWebToken


def setup_routes(app):
    app.router.add_get('/', ListDeviceView)
    app.router.add_get('/get_login/', GetLoginAndPassword)
    app.router.add_post('/get_token/', GetJsonWebToken)
