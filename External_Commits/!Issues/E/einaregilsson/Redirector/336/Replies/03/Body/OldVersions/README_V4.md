Because you didn't copy exactly what I wrote ![image](https://user-images.githubusercontent.com/43073868/213579696-6c5fb082-7deb-4c36-bde2-e6cd77878f77.png)

EDIT: actually strictly speaking it should be:

Include pattern: `(https?://\w+\.wikipedia\.org/wiki/.*)` Exclude pattern: `https?://\w+\.wikipedia\.org/wiki/.*?\?useskin=.*`

EDIT: simpler one with just wildcard match:

Include pattern: `http*://*.wikipedia.org/wiki/*` Redirect to: `http$1://$2.wikipedia.org/wiki/$3?useskin=timeless` Exclude pattern: `http*://*.wikipedia.org/wiki/*?useskin=*`
