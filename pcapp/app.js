var path = require('path');
const {app, BrowserWindow} = require('electron')
  function createWindow () {
    win = new BrowserWindow({
        width: 360, height: 640,
        webPreferences: {
            nodeIntegration: true,
            preload: path.resolve(path.join(__dirname, 'preload.js'))
        }
    });
    win.setMenu(null);
    win.loadFile('./index.html');
    win.webContents.session.clearCache(function(){});
  }
  app.on('ready', createWindow);
