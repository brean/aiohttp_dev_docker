"""basic setup for routing."""
from aiohttp import web
import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'name': 'User'}


def setup(app):
    app.add_routes([
        web.get(f'/', index)
    ])
