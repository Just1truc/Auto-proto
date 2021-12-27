#!/bin/sh
echo "=> Erase old versions..."
FILE=~/.auto-proto-script/
if [ -d $FILE ]
then
    sudo rm -rf ~/.auto-proto-script/
fi
tput setaf 2
echo "=> Done erasing old versions."
tput sgr 0
echo "=> Copying source code..."
mkdir ~/.auto-proto-script/
cp -R . ~/.auto-proto-script/
tput setaf 2
echo "=> Done copying source code."
tput sgr 0
echo "=> Adding zsh alias..."
OUTPUT=`cat ~/.zshrc | grep "alias auto-proto"`
if [[ $OUTPUT == "" ]]
then
    echo "alias auto-proto='sh ~/.auto-proto-script/auto-proto.sh'" >> ~/.zshrc
    tput setaf 2
    echo "=> Alias added."
    tput sgr 0
fi
tput setaf 2
echo "=> Installation complete."
tput sgr 0
echo "=> Restarting zsh..."
zsh
