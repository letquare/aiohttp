from app.api.views import ListDeviceView, GetLoginAndPassword, GetJsonWebToken, Hello


def setup_routes(app):
    app.router.add_get('/get_data/', ListDeviceView)
    app.router.add_get('/get_login/', GetLoginAndPassword)
    app.router.add_post('/get_token/', GetJsonWebToken)
    app.router.add_get('/hello/', Hello)
