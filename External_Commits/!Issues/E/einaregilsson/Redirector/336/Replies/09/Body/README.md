I don't know what the problem is then.

For the section title URLs, this wildcard works for me:

Include: `http*://*.wikipedia.org/wiki/*#*` Redirect: `http$1://$2.wikipedia.org/wiki/$3?useskin=timeless#$4` Exclude: `http*://*.wikipedia.org/*?useskin=*`

It needs to be placed before the other rule in the list.
