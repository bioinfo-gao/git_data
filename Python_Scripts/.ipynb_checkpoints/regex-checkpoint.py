<!doctype html><html lang="en"><head><meta charset="utf-8"><title>JupyterLab</title><meta name="viewport" content="width=device-width,initial-scale=1">   <script id="jupyter-config-data" type="application/json">{"allow_hidden_files": false, "appName": "JupyterLab", "appNamespace": "lab", "appSettingsDir": "C:/Users/zhen-/anaconda3/share/jupyter/lab/settings", "appUrl": "/lab", "appVersion": "4.0.11", "baseUrl": "/", "buildAvailable": true, "buildCheck": true, "cacheFiles": false, "copyAbsolutePath": false, "devMode": false, "disabledExtensions": ["jupyter-widgets-jupyterlab-manager", "jupyterlab-plotly"], "exposeAppInBrowser": false, "extensionManager": {"can_install": true, "install_path": "C:\\Users\\zhen-\\Anaconda3", "name": "PyPI"}, "extraLabextensionsPath": [], "federated_extensions": [{"extension": "./extension", "load": "static/remoteEntry.36690a2bfa9ee0dd7bc8.js", "mimeExtension": "./mimeExtension", "name": "jupyterlab-plotly"}, {"extension": "./extension", "load": "static/remoteEntry.ca1efc27dc965162ca86.js", "name": "@jupyter-widgets/jupyterlab-manager"}, {"extension": "./extension", "load": "static/remoteEntry.afbfa74351e195593c24.js", "name": "@jupyterlab-contrib/spellchecker", "style": "./style"}, {"extension": "./extension", "load": "static/remoteEntry.cfbccb113f4c7c1d65fe.js", "name": "@lckr/jupyterlab_variableinspector", "style": "./style"}, {"extension": "./extension", "load": "static/remoteEntry.c8393541423362724be3.js", "name": "@pyviz/jupyterlab_pyviz", "style": "./style"}], "fullAppUrl": "/lab", "fullLabextensionsUrl": "/lab/extensions", "fullLicensesUrl": "/lab/api/licenses", "fullListingsUrl": "/lab/api/listings", "fullMathjaxUrl": "/static/nbclassic/components/MathJax/MathJax.js", "fullSettingsUrl": "/lab/api/settings", "fullStaticUrl": "/static/lab", "fullThemesUrl": "/lab/api/themes", "fullTranslationsApiUrl": "/lab/api/translations", "fullTreeUrl": "/lab/tree", "fullWorkspacesApiUrl": "/lab/api/workspaces", "ignorePlugins": [], "labextensionsPath": ["C:\\Users\\zhen-\\AppData\\Roaming\\jupyter\\labextensions", "C:\\Users\\zhen-\\AppData\\Roaming\\Python\\share\\jupyter\\labextensions", "C:\\Users\\zhen-\\Anaconda3\\share\\jupyter\\labextensions", "C:\\ProgramData\\jupyter\\labextensions"], "labextensionsUrl": "/lab/extensions", "licensesUrl": "/lab/api/licenses", "listingsUrl": "/lab/api/listings", "mathjaxConfig": "TeX-AMS-MML_HTMLorMML-full,Safe", "mode": "multiple-document", "news": {"disabled": false}, "notebookStartsKernel": true, "notebookVersion": "[2, 14, 1]", "preferredPath": "/", "quitButton": true, "rootUri": "file:///c:/Users/zhen-", "schemasDir": "C:/Users/zhen-/anaconda3/share/jupyter/lab/schemas", "serverRoot": "C:/Users/zhen-", "settingsUrl": "/lab/api/settings", "staticDir": "C:/Users/zhen-/anaconda3/share/jupyter/lab/static", "store_id": 1, "templatesDir": "C:/Users/zhen-/anaconda3/share/jupyter/lab/static", "terminalsAvailable": true, "themesDir": "C:/Users/zhen-/anaconda3/share/jupyter/lab/themes", "themesUrl": "/lab/api/themes", "token": "f7d466092e9e8201f8695392dd66bc9ef121d620ea2d6593", "translationsApiUrl": "/lab/api/translations", "treePath": "Documents/Python_Scripts/Documents/Python_Scripts/Lynnda_Exercise_Files/09 Regexes/regex.py", "treeUrl": "/lab/tree", "userSettingsDir": "C:/Users/zhen-/.jupyter/lab/user-settings", "virtualDocumentsUri": "file:///c:/Users/zhen-/.virtual_documents", "workspace": "default", "workspacesApiUrl": "/lab/api/workspaces", "workspacesDir": "C:/Users/zhen-/.jupyter/lab/workspaces", "wsUrl": ""}</script><link rel="icon" type="image/x-icon" href="/static/favicons/favicon.ico" class="idle favicon"><link rel="" type="image/x-icon" href="/static/favicons/favicon-busy-1.ico" class="busy favicon"><script defer="defer" src="/static/lab/main.9dbb30dbd3113e5e36a2.js?v=9dbb30dbd3113e5e36a2"></script></head><body><script>/* Remove token from URL. */
  (function () {
    var location = window.location;
    var search = location.search;

    // If there is no query string, bail.
    if (search.length <= 1) {
      return;
    }

    // Rebuild the query string without the `token`.
    var query = '?' + search.slice(1).split('&')
      .filter(function (param) { return param.split('=')[0] !== 'token'; })
      .join('&');

    // Rebuild the URL with the new query string.
    var url = location.origin + location.pathname +
      (query !== '?' ? query : '') + location.hash;

    if (url === location.href) {
      return;
    }

    window.history.replaceState({ }, '', url);
  })();</script></body></html>