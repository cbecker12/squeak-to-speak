const socket = io(); 

const display = document.getElementById("display"); 

socket.on("display_update", (data) => {
    display.textContent = data.text; 
}); 

socket.on("connect", () => {
    socket.emit("register_client", {
        type: "display"
    });
}); 
