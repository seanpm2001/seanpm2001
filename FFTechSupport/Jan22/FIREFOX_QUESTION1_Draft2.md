
***

# Ubuntu Firefox garbage data increases exponentially

## Intro and context

Hello. I am a power user that works in software and web development. I have been using Firefox on and on for most my life, but full time as my main browser since late 2018. One thing I love Firefox for is its lightness on memory compared to that of Google Chrome, and also its open web standards and open source, privacy, ethical owners, and customizations. I have been using Windows 10 up until July 9th 2020 before I switched to my first main Linux desktop. I have always kept my eye on CPU and RAM usage, as high CPU drains battery and running out of RAM results in a system crash.
I actively keep many tabs open (less than 100 but more than 60) I ensure that they are light. I mostly have GitHub tabs open, but I keep a few other things open as well, mostly Wikipedia/wiktionary and duckduckgo tabs, a pcloud (file service) tab, but sometimes a youtube tab or two (rarely a reddit tab) 

## Issue

I have been noting that garbage collection is getting exponentially worse over time. When I got my laptop, I was able to keep 2-3 fully packed profiles open at all times, and never having to close Firefox until shutdown (after about 12-16 hours uptime) I rely heavily on Firefox profiles for organization. It has been getting exponentially worse. Starting in late 2020, I had to reduce the max number of open profiles to 2, and in 2021. In early January, I had to start closing the profiles once a day to free up 2-3+ GiB of RAM (swap doesn't change much, that is the garbage data that isn't being cleared, it normally ends up at 800 MiB to 1.7 GiB by the end of the day) and now (as of January 22nd 2021) I have to close Firefox 2-3 times a day to prevent my system from getting overloaded, as Firefox eats through 1-2 gigabytes of RAM per hour, even when idle. I have noticed several processes titled `web content` that use 200-600 MiB each (there is usually 2-7 of them) I am wondering what I can do for Firefox to prevent high RAM usage. For reference, here is my main profile in idle mode:

Mozilla is refusing to let me upload images right now, so I will link them

https://github.com/seanpm2001/seanpm2001/blob/master/FFTechSupport/Jan22/MProfile1_Idle_1.22.2021.png

Here is my usual 2nd profile in idle mode:

https://github.com/seanpm2001/seanpm2001/blob/master/FFTechSupport/Jan22/MProfile2_Idle_1.22.2021.png

Here is the RAM and SWAP usage before my 2nd refresh today (uptime: 8 hours 46 minutes)

https://github.com/seanpm2001/seanpm2001/blob/master/FFTechSupport/Jan22/FF_GF_Open_1.22.2021.png

And here it is with Firefox and Nautilus closed (I forgot about nautilus before getting the first 2 pics, it uses a lot of memory depending on its usage):

https://github.com/seanpm2001/seanpm2001/blob/master/FFTechSupport/Jan22/FF_GF_Closed_1.22.2021.png

I have lately suspected that GitHub may have gotten heavier, or is sending too much data via AJAX methods, but I am not entirely sure.

## System specs

Device: `Dell XPS 13 9XXX`

Operating system: `Ubuntu 20.04 (Focal Fossa)`

Linux Kernel version: `5.4.0-48-generic`

Processor type: `Intel Core i5 10th generation`

Processor specs: `Intel® Core™ i5-1035G1 CPU @ 1.00GHz × 8`

Processor mode: `x64`

Desktop environment: `GNOME 3.36.1`

Windowing system: `X Desktop environment 11`

Memory: `7.4 GiB (8 GB)`

SWAP file: `2.0 GiB`

Firefox version: `84.0.1` - I haven't updated in a while due to fear of memory increase and instability

Number of Firefox profiles: `61` - no new profiles created since December 26th 2020

I am wondering what I should do about this. I work with hundreds of projects, so I can't close too many tabs, as it becomes hard to access and manage. I intend to close 16 tabs in the next month, as I am freeing up some projects.

***

