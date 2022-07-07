from aiohttp import web

from app.api.routes import setup_routes as setup_api_routes
from app.settings import config
from app.store.database.accessor import PostgresAccessor


def setup_routes(application):
    setup_api_routes(application)


def setup_accessors(application):
    application['db'] = PostgresAccessor()
    application['db'].setup(application)


def setup_config(application):
    application['config'] = config


def setup_app(application):
    setup_config(application)
    setup_accessors(application)
    setup_routes(application)


app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    web.run_app(app, port=config['common']['port'])
