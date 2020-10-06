import os


def redishost_processor(request):
    return {'redishost': os.environ.get('REDISHOST', '127.0.0.1:8000')}
