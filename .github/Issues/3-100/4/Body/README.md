***

### Gitattributes documentation

I have grown to like Gitattributes files. Something has always confused me about them though, which is how the `-linguist-detectable` works, but using `linguist-documentation` on true never works.

Here is an example:

Working YAML detection

```gitattributes
*.yml linguist-detectable=true
*.yml linguist-documentation=false
*.yaml linguist-detectable=true
*.yaml linguist-documentation=false
```

Non-Working YAML detection

```gitattributes
*.yml linguist-detectable=true
*.yml linguist-documentation=true
*.yaml linguist-detectable=true
*.yaml linguist-documentation=true
```

What does documentation mean in this sense?

***
