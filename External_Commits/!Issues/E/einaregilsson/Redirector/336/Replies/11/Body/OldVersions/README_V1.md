If this helps, here is my JSON configuration file.
GitHub isn't letting me import it, so here is the source:

```json
{
    "createdBy": "Redirector v3.5.3",
    "createdAt": "2023-01-19T23:53:57.174Z",
    "redirects": [
        {
            "description": "Anti-Google",
            "exampleUrl": "https://google.com",
            "exampleResult": "https://duckduckgo.com",
            "error": null,
            "includePattern": "https://google.com",
            "excludePattern": "",
            "patternDesc": "In case you ever make the mistake",
            "redirectUrl": "https://duckduckgo.com",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": false,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "De-mobilize Wikipedia links",
            "exampleUrl": "https://en.m.wikipedia.org/",
            "exampleResult": "https://en.wikipedia.org",
            "error": null,
            "includePattern": "https://en.m.wikipedia.org/",
            "excludePattern": "",
            "patternDesc": "Wikipedia De-Mobilizer",
            "redirectUrl": "https://en.wikipedia.org",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia fix 2023 (2)",
            "exampleUrl": "https://en\\.wikipedia\\.org/([^?]*)$",
            "exampleResult": "https://en.wikipedia.org/*?useskin=vector",
            "error": null,
            "includePattern": "https://en\\.wikipedia\\.org/([^?]*)$",
            "excludePattern": "",
            "patternDesc": "",
            "redirectUrl": "https://en.wikipedia.org/$1?useskin=vector",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia redirect test 2",
            "exampleUrl": "https://en.wikipedia.org/wiki/",
            "exampleResult": "?useskin=monobook",
            "error": null,
            "includePattern": "https://en.wikipedia.org/wiki/",
            "excludePattern": "",
            "patternDesc": "",
            "redirectUrl": "?useskin=monobook",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "https://https://en.wikipedia.org/wiki/",
            "exampleUrl": "https://en.wikipedia.org/wiki/",
            "exampleResult": "https://en.wikipedia.org/wiki/?useskin=monobook",
            "error": null,
            "includePattern": "https://en.wikipedia.org/wiki/",
            "excludePattern": "",
            "patternDesc": "Wikipedia fix ",
            "redirectUrl": "https://en.wikipedia.org/wiki/?useskin=monobook",
            "patternType": "R",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia fix 2023",
            "exampleUrl": "^https://en\\.wikipedia\\.org/([^?]*)$",
            "exampleResult": "https://en.wikipedia.org/*?useskin=vector",
            "error": null,
            "includePattern": "^https://en\\.wikipedia\\.org/([^?]*)$",
            "excludePattern": "",
            "patternDesc": "",
            "redirectUrl": "https://en.wikipedia.org/$1?useskin=vector",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia vector 2022 fix (2023, January 19th)",
            "exampleUrl": "(https?://\\w+.en.wikipedia.org/wiki/.*)",
            "exampleResult": "(https?://\\w+.wikipedia.org/wiki/.*?useskin=monobook*)",
            "error": null,
            "includePattern": "(https?://\\w+.en.wikipedia.org/wiki/.*)",
            "excludePattern": "https?://\\w+.wikipedia.org/wiki/.*?\\?useskin=.*",
            "patternDesc": "Attempted fix from a GitHub user",
            "redirectUrl": "(https?://\\w+.wikipedia.org/wiki/.$1?useskin=monobook*)",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia vector 2022 fix (2023, January 19th) (v2)",
            "exampleUrl": "(https?://\\w+.wikipedia.org/wiki/.*)",
            "exampleResult": "*?useskin=monobook",
            "error": null,
            "includePattern": "(https?://\\w+.wikipedia.org/wiki/.*)",
            "excludePattern": "https?://\\w+.wikipedia.org/wiki/.*?\\?useskin=.*",
            "patternDesc": "Attempted fix from a GitHub user",
            "redirectUrl": "$1?useskin=monobook",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia vector 2022 fix (2023, January 19th) (v3)",
            "exampleUrl": "(https?://\\w+.wikipedia.org/wiki/.*)",
            "exampleResult": "(https?://\\w+.wikipedia.org/*?useskin=monobook",
            "error": null,
            "includePattern": "(https?://\\w+.wikipedia.org/wiki/.*)",
            "excludePattern": "https?://\\w+.wikipedia.org/wiki/.*?\\?useskin=.*",
            "patternDesc": "Attempted fix from a GitHub user",
            "redirectUrl": "(https?://\\w+.wikipedia.org/$1?useskin=monobook",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia monobook theme",
            "exampleUrl": "https://en.wikipedia.org/wiki/cat/",
            "exampleResult": "https://en.wikipedia.org/wiki/cat/?useskin=monobook",
            "error": null,
            "includePattern": "http*://*.wikipedia.org/wiki/*",
            "excludePattern": "https?://\\w+\\.wikipedia\\.org/wiki/.*?\\?useskin=.*",
            "patternDesc": "Wikipedia Monobook theme",
            "redirectUrl": "http$1://$2.wikipedia.org/wiki/$3?useskin=monobook",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": false,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia vector (old) theme",
            "exampleUrl": "https://en.wikipedia.org/wiki/cat/",
            "exampleResult": "https://en.wikipedia.org/wiki/cat/?useskin=vector",
            "error": null,
            "includePattern": "http*://*.wikipedia.org/wiki/*",
            "excludePattern": "https?://\\w+\\.wikipedia\\.org/wiki/.*?\\?useskin=.*",
            "patternDesc": "Wikipedia old vector theme",
            "redirectUrl": "http$1://$2.wikipedia.org/wiki/$3?useskin=vector",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia timeless theme",
            "exampleUrl": "https://en.wikipedia.org/wiki/cat/",
            "exampleResult": "https://en.wikipedia.org/wiki/cat/?useskin=timeless",
            "error": null,
            "includePattern": "http*://*.wikipedia.org/wiki/*",
            "excludePattern": "https?://\\w+\\.wikipedia\\.org/wiki/.*?\\?useskin=.*",
            "patternDesc": "Wikipedia timeless theme",
            "redirectUrl": "http$1://$2.wikipedia.org/wiki/$3?useskin=timeless",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        },
        {
            "description": "Wikipedia vector 2022 fix (2023, January 19th) (v3)",
            "exampleUrl": "(https?://\\w+.wikipedia.org/wiki/.*)",
            "exampleResult": "(https?://\\w+.wikipedia.org/*?useskin=monobook",
            "error": null,
            "includePattern": "(https?://\\w+.wikipedia.org/wiki/.*)",
            "excludePattern": "(https?://\\w+.wikipedia.org/wiki/.*?\\?useskin=.*)",
            "patternDesc": "Attempted fix from a GitHub user",
            "redirectUrl": "(https?://\\w+.wikipedia.org/$1?useskin=monobook",
            "patternType": "W",
            "processMatches": "noProcessing",
            "disabled": true,
            "grouped": false,
            "appliesTo": [
                "main_frame"
            ]
        }
    ]
}
```
