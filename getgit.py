print ('do you get git?')

# to configure my information
git config --global user.name 'Steve Shay'
git config --global user.email 'myemail@myemail.com'

# initialize a new local respository
git init

# Working with a GitHub repository on local
git clone https://github.com/username/repository.git
git remote #see the remote repositories by name
git push [specify remote name if multiple] #pushes new files and changes to remote
git pull

# some basic commands
git status #see which files have changes or are untracked

git add filename.txt #add specific file to version control
git add *.txt #add all .txt files
git add . #add all files
git commit -m 'commit comment title' -m 'commit comment details'

# create a new branch and switch to it
git branch mybranch
git checkout mybranch
