#!/usr/bin/env python3
"""Start webserver."""

import os
import asyncio
from aiohttp import web
import aiohttp_jinja2
import jinja2
from .routes.setup import setup as routes_setup


async def create_app() -> web.Application:
    """Connect to database and create web application."""
    app = web.Application()
    setup_jinja2(app)
    routes_setup(app)
    app.update(static_root_url='/static/')
    return app


def setup_jinja2(app):
    """Jinja2 setup."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_path, 'templates')
    jinja2_loader = jinja2.FileSystemLoader(template_path)
    aiohttp_jinja2.setup(app, loader=jinja2_loader)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = loop.run_until_complete(create_app(True))
    web.run_app(app)
