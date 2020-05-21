import asyncio
import socketio

mgr = socketio.AsyncRedisManager('redis://redis:6379/0')
sio_app = socketio.AsyncServer(async_mode='asgi', client_manager=mgr)

@sio_app.event
async def connect(sid, environ):
    print("connect ", sid)

@sio_app.event
async def disconnect(sid):
    print('disconnect ', sid)

@sio_app.event
async def ping_from_client(sid):
    await sio_app.emit('pong_from_server', room=sid)
