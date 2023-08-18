I have noticed some very strange behavior in [:octocat: one of my repositories:](https://github.com/seanpm2001/Git-Templates/)

![NegativeLanguageUsage_GitHub-Git-Templates_2023July14th](https://github.com/github-linguist/linguist/assets/65933340/428367db-6bf1-483f-b70e-c65262d2a23a)

So some background context: this repository contains snippets and template source code for thousands of my repositories, and has source code in over 500 different programming languages (I am a language collector)

Yesterday, I went to look at the Linguist. C++ is one of the top 7 languages in the project, but has been at the very top of the Linguist for a while. It has been rapidly dropping, while the second value has remained a higher percentage the whole time (it has been `0.1% C++`, `3.5% HTML`, `2.3% C`, `2.3% R`, `2.1% Python`, `1.4% "Forth"` (just a mixture of languages that share the `*.f` file extension, Forth isn't very much of this) and `88.3% Other` as of the day before) I noticed that instead of reporting `0.1%`, or `0.0% C++` usage, it is reporting **negative** `0.1% C++` usage. How was this even allowed to happen? You can't have negative percentage language usage. It should have been merged into the 88.4% other at this point, although the numbers would add up to 100% it still isn't correct.

I don't entirely know if this is going to be fixed, but I found it kind of funny.
