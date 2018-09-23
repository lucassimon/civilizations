# Python
import asyncio
import logging
import sys
# Third
import aioredis
from aioredis import ConnectionsPool
from vibora import Request, Vibora
from vibora.blueprints import Blueprint
from vibora.hooks import Events
from vibora.responses import JsonResponse, Response, StreamingResponse

# Local
from .config import Config

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)7s: %(message)s',
    stream=sys.stderr,
)

logger = logging.getLogger('')

api = Blueprint()


@api.route('/')
async def index(pool: ConnectionsPool):
    await pool.set('my_key', 'any_value')
    value = await pool.get('my_key')
    return Response(value.encode())


@api.route('/home')
async def home(request: Request):
    logger.info('ola')
    return JsonResponse({'hello': 'world'})


@api.route('/stream')
async def stream(request: Request):
    async def stream_builder():
        for x in range(0, 5):
            yield str(x).encode()
            await asyncio.sleep(1)

    return StreamingResponse(
        stream_builder, chunk_timeout=10, complete_timeout=30
    )


@api.handle(Events.BEFORE_SERVER_START)
async def initialize_db(app: Vibora, config: Config):

    # Creating a pool of connection to Redis.
    pool = await aioredis.create_pool(config.REDIS_HOST)

    # In this case we are registering the pool as a new component
    # but if you find yourself using too many components
    # feel free to wrap them all inside a single component
    # so you don't need to repeat yourself in every route.
    app.components.add(pool)
