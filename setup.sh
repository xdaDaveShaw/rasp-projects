#!/usr/bin/env bash

#Unzip SSH keys
cd ~/Downloads
if [ ! -f SSH.zip ]; then
    echo "SSH Keys not found in ~/Downloads"
    exit 0
fi
unzip SSH.zip -d ~/.ssh/
rm SSH.zip

#Install latest updates
sudo apt-get update --yes
sudo apt-get dist-upgrade --yes

#Set timezone
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/Europe/London /etc/localtime
sudo rm /etc/timezone
echo "Europe/London" | sudo tee /etc/timezone 

#Install Useful Tools
sudo apt-get install git --yes
sudo apt-get install vim --yes
sudo apt-get install python3-pip --yes

# GPIO Zero
sudo apt install python3-gpiozero python-gpiozero --yes

#Cleanup
sudo apt-get autoremove --yes
sudo apt-get clean --yes

#Setup SSH
cd ~
sudo chmod 700 /.ssh
cd ~/.ssh
sudo chmod 600 id_rsa
sudo chmod 600 id_rsa.pub
sudo chmod 600 known_hosts
eval "$(ssh-agent -s)"
ssh-add

#Download Code
cd ~
git clone git@github.com:xdaDaveShaw/rasp-projects.git projects

#Configure git
git config --global alias.co 'checkout'
git config --global alias.rbom '!f() { DEFAULT=$(git default); git rebase origin/$DEFAULT $1; }; f'
git config --global alias.rbc 'rebase --continue'
git config --global alias.sw 'switch'
git config --global alias.ec 'config --global -e'
git config --global alias.up '!git pull --rebase --prune $@ && git submodule update --init --recursive'
git config --global alias.cob 'checkout -b'
git config --global alias.cm '!git add -A && git commit'
git config --global alias.cmm '!git add -A && git commit -m'
git config --global alias.save '!git add -A && git commit -m "SAVEPOINT"'
git config --global alias.wip '!git add -u && git commit -m "WIP"'
git config --global alias.undo 'reset HEAD~1 --mixed'
git config --global alias.amend 'commit -a --amend'
git config --global alias.default '!git symbolic-ref refs/remotes/origin/HEAD | sed "s@^refs/remotes/origin/@@"'
git config --global alias.wipe '!git add -A && git commit -qm "WIPE SAVEPOINT" && git reset HEAD~1 --hard'
git config --global alias.bclean '!f() { git branch --merged ${1} | grep -v " ${1}$" | xargs -r git branch -d; }; f'
git config --global alias.bdone '!f() { DEFAULT=$(git default); git checkout ${1-$DEFAULT} && git up && git bclean ${1-$DEFAULT}; }; f'

git config --global alias.lol 'log --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset" --abbrev-commit'
git config --global alias.lola 'log --all --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset" --abbrev-commit'
git config --global alias.logg 'log --graph --all --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%ar) %C(bold blue)<%an>%Creset" --abbrev-commit'

git config --global alias.web '!f() { git ls-remote --get-url origin; }; u=$(f); start $u'

git config --global core.editor "vim"
git config --global user.email "dave@taeguk.co.uk"
git config --global user.name "Dave Shaw"
git config --global push.default simple
