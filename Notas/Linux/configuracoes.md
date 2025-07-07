
## GIT

### Configurações Globais

```sh
git config --global user.name "Breno Cabral"

git config --global user.email "breno.ara.cabral@gmail.com"

git config --global init.defaultBranch "main"
```

### Gerar Chave GitHub

```sh
ssh-keygen -t ed25519 -C "breno.ara.cabral@gmail.com" -f ~/.ssh/github

eval "$(ssh-agent -s)"

ssh-add ~/.ssh/github

cat ~/.ssh/github.pub
```

## ZSH

### Fedora Installation

```sh
sudo dnf install zsh
```

### Nerd Fonts

Baixe Roboto FiraCode e coloque em `~/.local/share/fonts`  
[Nerd Fonts - Download](https://www.nerdfonts.com/font-downloads)

```sh
fc-cache -f -v
```

Usar gnome tweaks para configurar fonte global

### Powerlevel10k

```sh
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.zsh/powerlevel10k

echo 'source ~/.zsh/powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc
```

### Autosuggest

```sh
git clone https://github.com/zsh-users/zsh-autosuggestions.git ~/.zsh/autosuggestions

echo '#Autosuggest' >> ~/.zshrc

echo 'source ~/.zsh/autosuggestions/zsh-autosuggestions.zsh' >> ~/.zshrc
```

### Syntax Highlighting

```sh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/syntax-highlighting

echo '#Syntax Highlighting' >> ~/.zshrc

echo 'source ~/.zsh/syntax-highlighting/zsh-syntax-highlighting.zsh' >> ~/.zshrc
```

