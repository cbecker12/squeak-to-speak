const socket = io();

socket.on("connect", () => {

    socket.emit("register_client", {
        type: "admin"
    });

});

socket.on("update_admin", (data) => {

    console.log(data);

    document.getElementById("keyboard-status").textContent =
        data.keyboard_running ? "Listening" : "Stopped";

    document.getElementById("display-count").textContent =
        data.display_clients;

    document.getElementById("control-count").textContent =
        data.control_clients;

    document.getElementById("last-key").textContent =
        data.last_key;

    document.getElementById("last-emoji").textContent =
        data.last_emoji;

    document.getElementById("current-buffer").textContent =
        data.buffer;

    const baseUrl = `http://${data.local_ip}:${data.port}`;

    document.getElementById("display-url").textContent =
        `${baseUrl}/display`;

    document.getElementById("control-url").textContent =
        `${baseUrl}/control`;

    document.getElementById("admin-url").textContent =
        `${baseUrl}/admin`;

}); 