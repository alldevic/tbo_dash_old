import socketio

mgr = socketio.AsyncRedisManager('redis://redis:6379/0')
sio_app = socketio.AsyncServer(async_mode='asgi',
                               client_manager=mgr,
                               ping_interval=3,
                               cors_allowed_origins='*')


@sio_app.event
async def connect(sid, environ):
    print("connect ", sid)


@sio_app.event
async def disconnect(sid):
    print('disconnect ', sid)
