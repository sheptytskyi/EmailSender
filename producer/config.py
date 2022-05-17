from starlette.config import Config

config = Config('.env')

DATABASE_URI = config('DATABASE_URI', cast=str, default='sqlite:///test.db')
PARAMS = config('PARAMS', cast=str, default='localhost')
QUEUE = config('QUEUE', cast=str, default='test-queue')
