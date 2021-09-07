***

### How to make files format in soft wrap with editorconfig files

I have started using `.editorconfig` files ever since I learned about them when tinkering with the snapcraft fork and rename me project. I am not sure if my .`editorconfig` files work, but I have been trying to add a special clause to make text wrap. It is not identified as valid syntax, here is an example:

```editorconfig
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = false
insert_final_newline = false
line_wrap_mode = soft wrap

[*.md]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = false
insert_final_newline = false
line_wrap_mode = soft wrap
```

What is the correct way of fixing the last line of each block?

***
