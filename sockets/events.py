from flask import request

from extensions import socketio

import services.emoji_service as emoji_service

from shared.constants import *
from shared.state import ServerState

from sockets.emitter import update_admin


client_types = {}


@socketio.on("connect")
def connect():
    print(f"Connected: {request.sid}")


@socketio.on("disconnect")
def disconnect():
    client_type = client_types.pop(request.sid, None)

    if client_type == "display":
        ServerState.display_clients = max(
            0,
            ServerState.display_clients - 1
        )

    elif client_type == "control":
        ServerState.control_clients = max(
            0,
            ServerState.control_clients - 1
        )

    update_admin()

    print(f"Disconnected: {request.sid}")


@socketio.on(ADD_EMOJI)
def add_emoji(data):
    emoji_service.add_emoji(data["emoji"])


@socketio.on(CLEAR_DISPLAY)
def clear_display():
    emoji_service.clear()


@socketio.on(UNDO)
def undo():
    emoji_service.undo()


@socketio.on("register_client")
def register_client(data):
    client_type = data.get("type")

    client_types[request.sid] = client_type

    if client_type == "display":
        ServerState.display_clients += 1

    elif client_type == "control":
        ServerState.control_clients += 1

    elif client_type == "admin":
        # Dashboard only; no client count needed.
        pass

    update_admin()