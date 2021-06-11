@ECHO OFF
TITLE Squash and Rebase
ECHO This will Squash your work into one commit in the git
::ECHO ONLY PROCEED IF YOU HAVE TESTED ::
PAUSE
ECHO ENTER THE BRANCH NAME YOU ARE WORKING ON EXACTLY
SET /P branchname="ENTER BRANCH NAME: "
PAUSE
::get last commit SHA::
SET last_commit_SHA=$(git rev-parse HEAD)
::squash into 1 commit::
git rebase -i %last_commit_SHA%
::push to remote::
git push origin %branchname% --force

ECHO IF ALL YOU WANT TO DO IS SQUASH THEN DO NOT PROCEED AND EXIT
ECHO IF YOU PROCEED YOU WILL COMMIT AND MERGE TO MASTER
PAUSE
git checkout master
git pull origin master
git checkout %branchname%
git rebase master
git push origin %branchname% --force
git checkout master
git merge %branchname%
git push origin master
PAUSE