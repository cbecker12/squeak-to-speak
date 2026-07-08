from flask import Flask 
from extensions import socketio 
import threading 
from shared.network import get_local_ip 
from config import HOST, PORT 
from shared.state import ServerState 

def print_startup_banner(): 
    ip = get_local_ip() 
    ServerState.local_ip = ip 

    print() 
    print("-" * 45) 
    print("      Squeak to Speak v1.0") 
    print("-" * 45) 
    print() 
    print("Server started successfully") 
    print() 
    print(f"Display: http://{ip}:{PORT}/display") 
    print(f"Control: http://{ip}:{PORT}/control") 
    print(f"Admin: http://{ip}:{PORT}/admin") 
    print() 
    print("Press Ctrl+C to stop the server.") 
    print() 
    print("-" * 45) 

def create_app(): 
    app = Flask(__name__) 

    app.config["SECRET_KEY"] = "change-this-later"
    socketio.init_app(app) 

    from routes.display import display_bp 
    from routes.control import control_bp 
    from routes.admin import admin_bp 

    app.register_blueprint(display_bp) 
    app.register_blueprint(control_bp) 
    app.register_blueprint(admin_bp) 

    import sockets.events 

    from services.keyboard_service import start 
    thread = threading.Thread( 
        target=start, 
        daemon=True 
    ) 
    thread.start() 

    return app 

if __name__ == "__main__": 
    app = create_app() 
    
    print_startup_banner() 

    socketio.run( 
        app, 
        host=HOST, 
        port=PORT, 
        debug=True,
    ) 