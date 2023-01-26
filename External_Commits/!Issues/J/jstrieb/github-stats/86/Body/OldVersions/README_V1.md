I have an iteration of the GitHub stats repository, which I made heavy modifications to. I didn't update any of the build files (except for recently, when I attempted to update the action manually) but my workflow hasn't been successful at all for over a month now.

Originally, the workflow worked either partially or fully almost every day, with up to 3 consecutive days of failure at a time. However, the last successful run was on 2022, December 20th (it wasn't a full success either, the last full success was on 2022, December 12th) to see successful runs [`go here`](https://github.com/seanpm2001/GitHub_Stats_A/tree/master/Seasons/) (note: the current season is [`7`](https://github.com/seanpm2001/GitHub_Stats_A/tree/master/Seasons/7/) the last season with successful runs was [`6`](https://github.com/seanpm2001/GitHub_Stats_A/tree/master/Seasons/6/))

The workflow usually takes 1-3.5 hours to finish. I assume it is because of how many projects I have. I am curious if this workflow was designed for users with over 2500 source repositories.

I don't know what went wrong, but I keep daily logs of the status of the repository. @jstrieb is it possible for you to check and see if I did something that may have screwed up the workflow?

I have been using the same setup method for the access token, configuring it monthly.

The repository is located [`here`](https://github.com/seanpm2001/GitHub_Stats_A/) workflow log archives are located [`here`](https://github.com/seanpm2001/GitHub_Stats_A/tree/master/ErrorLog/) This message is a bit long. Here is a summary:

**TL;DR** _workflow hasn't ran successfully in over a month, may need manual inspection_
