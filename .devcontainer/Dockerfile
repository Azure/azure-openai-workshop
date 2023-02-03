# Using the azure CLI container so we dont have to install that to start
FROM mcr.microsoft.com/azure-cli
    
RUN apk update

# Install tools
RUN apk add nano vim tcpdump tmux jq curl

RUN apk add zsh \
&& sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
