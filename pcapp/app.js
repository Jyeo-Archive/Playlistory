const {app, BrowserWindow} = require('electron')
  function createWindow () {
    win = new BrowserWindow({
        width: 360, height: 640,
        webPreferences: {
            zoomFactor: 3.0,
            nodeIntegration: false
        }
    });
    win.setMenu(null);
    win.loadFile('./index.html');
  }
  app.on('ready', createWindow);
