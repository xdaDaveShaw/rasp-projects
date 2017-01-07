#Install VIM
sudo apt-get install vim --yes

#Setup SSH
cd ~
chmod 700 /.ssh
cd ~/.ssh
chmod 600 id_rsa
chmod 600 id_rsa.pub
chmod 600 known_hosts
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
