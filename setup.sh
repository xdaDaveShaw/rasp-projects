#!/bin/bash

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
sudo apt-get install vim --yes

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
git config --global alias.co "checkout"
git config --global alias.ec "config --global -e"
git config --global alias.cm "!git add -A && git commit -m"
git config --global alias.cob "checkout -b"
git config --global alias.up "!git pull --rebase --prune $@ && git submodule update --init --recursive"
git config --global alias.bclean  "!f() { git branch --merged ${1-master} | grep -v " ${1-master}$" | xargs -r git branch -d; }; f"
git config --global alias.bdone "!f() { git checkout ${1-master} && git up && git bclean ${1-master}; }; f"
git config --global core.editor "vim"
git config --global user.email "dave@taeguk.co.uk"
git config --global user.name "Dave Shaw"
git config --global push.default simple
