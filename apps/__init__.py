# -*- coding: utf-8 -*-

# Python Libs.

from vibora import Vibora, Response
# -*- coding: utf-8 -*-

from vibora.hooks import Events

from .config import config
from .api import api


def create_app(config_name):
    app = Vibora()

    @app.handle(Events.AFTER_ENDPOINT)
    async def before_response(response: Response):
        response.headers['x-my-custom-header'] = 'Hello :)'

    app.components.add(config[config_name]())

    app.add_blueprint(api, prefixes={'v1': '/v1'})

    return app
