from flask import Flask 
from flask_socketio import SocketIO 

# Global instance 
socketio = SocketIO() 

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

    return app 

if __name__ == "__main__": 
    app = create_app() 
    
    socketio.run( 
        app, 
        host="0.0.0.0", 
        port=5000, 
        debug=True,
    ) 
