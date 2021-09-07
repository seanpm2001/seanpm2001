***

### How do I create submodules?

I have been trying to create a submodule for several months, and I have gotten close but didn't succeed.

Here is a sample:

```gitmodules
[submodule "Torvalds/Linux"]
	path = WacOS/Kernel/Linux5.7
	url = https://github.com/torvalds/linux
```

File name: `.gitmodules`

The goal is to create a folder/module that when clicked will take you to https://github.com/torvalds/linux 

I have tried many methods, and I just can't create one. The closest I have gotten was this, and I received an error (file could not be created)

![Submodule_Fail_2021September6th_LightMode_1080p](https://user-images.githubusercontent.com/65933340/132275651-ec26cea4-11a9-40c9-b3c1-4d59b9b76c31.png)

I am using GitHub through the Firefox web browser on Linux, and I do not have Git installed. I can't install Git at the moment, as I already messed up my last laptop when installing SAMBA, and I don't want to mess this one up as well. Is there any way to make a submodule with the browser? If not, what is a good resource for creating one? I have tried the guide on https://git-scm.com/ but it didn't help much.

***
