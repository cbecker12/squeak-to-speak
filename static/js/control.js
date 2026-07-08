const socket = io(); 

function sendEmoji(emoji) { 
    socket.emit("add_emoji", {
        emoji: emoji 
    }); 
} 

function clearDisplay() { 
    socket.emit("clear_display"); 
} 

function undo() { 
    socket.emit("undo"); 
} 

socket.on("connect", () => {
    socket.emit("register_client", {
        type: "control"
    });
});