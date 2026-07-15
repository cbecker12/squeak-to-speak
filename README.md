# Squeak to Speak 

Made by Chris Becker - chrisbecker1206@gmail.com 

REQUIREMENTS: 
    -Windows OS 
    -A connected keyboard 
    -Devices to use the control and admin pages with 

##### 

STARTING THE SERVER: 
    -Double click SqueakToSpeak.exe 
    -The console will display three URLs for the display, control, and admin pages 

##### 

EDITING KEYBOARD MAPPINGS: 
    -Open config.json and add or change key mappings then restart the server 

##### 

BUNDLING WITH PYINSTALLER: 

pyinstaller \
    --onedir \
    --name SqueakToSpeak \
    --hidden-import keyboard \
    --hidden-import engineio.async_drivers.threading \
    --add-data "templates:templates" \
    --add-data "static:static" \
    app.py 

Put config.json next to the created dist/SqueakToSpeak/SqueakToSpeak.exe file. 