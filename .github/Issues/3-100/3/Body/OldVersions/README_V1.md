***

# What is the point of a GITIGNORE file

I have been using Gitignore files in my projects as vanity files for a long time not knowing what they do. I originally thought it was just to ignore certain files, so I configured most of them to the Go language.

That may not be the case. I am wondering what a `.gitignore` files does, and how it differs from a `.gitattributes` file.

For example, a `.gitattributes` file can ignore a YAML file like so:

```gitattributes
*.yml linguist-detectable=false
*.yml linguist-documentation=false
*.yaml linguist-detectable=false
*.yaml linguist-documentation=false
```

So what is the point of a `.gitignore` file?

***
