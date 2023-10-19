
Members:
1. Palm
2. Pokpong
3. Peach
4. Blue

# First Practice (Palm, Pokpong):

## Team A (Palm):
It was my first time using Git. I was introduced to the very basic things like initializing repositories and creating commits to more advanced things like branching and resolving conflicts. It helps with structuring how you work, share code, and manage projects efficiently. Also make the chaotic process of code collaboration organized. The thing that surprised me the most was Git doesn’t require an internet connection to work, you can make commits and perform many things offline. Another thing was to commit before sharing, normally I would just commit and if I made a mistake, I would just delete and recommit. Git doesn’t immediately share the changes with others. You need to commit them first. This provides a level of control over what gets shared and what doesn’t.

## Team B (Pokpong):

What confused me initially was how to resolve conflicts, since there was no guide or suggestions on how to fix it at all. It turns out it was just a matter of using a text editor to incorporate the differences the way we want.

One thing that I didn’t expect was when git automatically merged the side branch to the main branch when I pulled the side branch while on the main branch. In hindsight it seems to make sense since pull, in my understanding, will not remove or replace the files locally.

Some other things I noticed is that the command `git branch -d` only removes locally. In order to remove the branch in the remote repository I had to use the command `git push -d <remote repository link>  <branch name>`.

# Second Practice (Peach, Blue):

## Team A (Peach):
I wouldn't say I am new to Git. I have used some of Git's functionalities before, such as Push, Pull, and Commit. This lab, however, has introduced me to the advanced level of Git, which includes merging, restoring, and resolving conflicts. I have realized that sometimes the best approach is to create different branches for each team member to work on their code, allowing them to modify the code while keeping the main code intact. This way, we can ensure that the main code is not polluted. If anything, I have also learned that we should always save the code before we commit since my VS Code editor didn't automatically save the code. This is the most crucial lesson I have learned because, God forbid, I have spent more than 40 minutes trying to figure out what went wrong, while the culprit was just the "saving" command.

## Team B (Blue):

1. Before you edit the code that you work with the team, you should not forget to pull the up-to-date repository.

2. If you want to revert your code or file, you should know the serial number of each version you want to go back to. You can check for it by using `git log`.

3. Every time you edit any files, the status will show that the file is modified. If you are satisfied with the change, you need to add the file every time before you commit.

4. There are 3 main states: modified, staged, and committed.
	- Modified = the file is changed and has not been committed yet.
	- Staged = marking the modified file in its current version.
	- Committed = the data is already in the local database.

6. If you want to push the local data to GitHub, you need to use the command `git push`.
