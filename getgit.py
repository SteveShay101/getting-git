print ('do you get git?')

# to configure my information
git config --global user.name 'Steve Shay'
git config --global user.email 'myemail@myemail.com'

# initialize a new respository
git init

# some basic commands
git status
git add filename.txt #add specific file to version control
git add *.txt #add all .txt files
git add . #add all files
git commit -m 'commit comment title' -m 'commit comment details'


# create a new branch and switch to it
git branch mybranch
git checkout mybranch
