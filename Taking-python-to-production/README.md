

## 1. ZSH setup (cheat sheet)

# update apt-get so it will install the most up-to-date versions of packages
apt-get update
 
# try to install sed, git, and zsh if they aren't already present
# Note: sed is a command for editing text files, we will use it further down
# to configure the ~/.zshrc file
which sed || sudo apt-get install -y sed || echo "linux: could not install sed"
which zsh || sudo apt-get install -y zsh || echo "linux: could not install zsh"
which git \
    || sudo add-apt-repository ppa:git-core/ppa \
    && sudo apt-get update \
    && sudo apt-get install -y git \
    || echo "mac: could not install git"
 
# install OhMyZSH if it isn't already installed
[ -d ~/.oh-my-zsh ] || sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
 
# plugin: zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
 
# plugin: zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
 
# add these two plugins and enable some of the default ones
sed -i 's/\(^plugins=([^)]*\)/\1 python pip pyenv virtualenv web-search zsh-autosuggestions zsh-syntax-highlighting/' "$HOME/.zshrc"
 
# set the ZSH_THEME to "bira"
sed -i 's/_THEME=\".*\"/_THEME=\"bira\"/g' "$HOME/.zshrc"




## 2. Principles of clean code (PEP 8)

https://peps.python.org/pep-0008/

Principles of clean code. 

- Code based in readability. 
    - Don't use comments.
- Functions based in inputs.
    - Don't relay in global states.


Resources:
    - testdriven.io


Code Quality:
    - Does it work?
    - Can be understood?
    - Is it safe?
    - Do we even want this?
        - More code more to maintain.
    - Keep commits and PR small for review.

.vscode style format
- sttings.json - black extension in vscode.
- Pylint
    - Improves readability and cleaner code. 
- Mypy 
    - Static Python -
        settings.json
        "python.Linting.Enabled:"

- typing library ()
    - Improves readibility of elements
    - Tuples, Classes, 
 