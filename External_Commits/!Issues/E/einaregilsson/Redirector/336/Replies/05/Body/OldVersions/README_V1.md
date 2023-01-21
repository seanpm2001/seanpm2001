I can't get that to happen for me. Do you have more info?

Also I forgot there are other forms for article urls, like `https://en.wikipedia.org/w/index.php?title=Cat`, this wildcard pattern will do:

Include: `http*://*.wikipedia.org/w/index.php?title=*` Redirect: `http$1://$2.wikipedia.org/wiki/$3?useskin=timeless`
