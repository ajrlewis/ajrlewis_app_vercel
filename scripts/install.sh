#! /usr/bin/env bash

help() {
   echo "Syntax: bash install.sh [-d|h]"
   echo "options:"
   echo "d     Enable development mode."
   echo "h     Print this help."
   echo
}

environment="prod";

while getopts ":dht:" option; do
    case $option in
        d) # set development mode
            environment="dev";;
        h) # display help
            help;
            exit;;
        \?) # Invalid option
            echo "Error: Invalid option"
            exit;;
   esac
done

# Create virtual environment
if [[ $environment == "dev" ]]; then
    
    if [ ! -d venv ]; then
        echo ">> Creating virtual environment.";
        python3.9 -m venv venv;
    fi;
    echo ">> Activating virtual environment."
    source venv/bin/activate;
    echo ">> Sourcing environmental variables."
    source .env;
fi

# Install dependencies
echo ">> Upgrading pip."
pip install --upgrade pip;
echo ">> Installing requirements."
pip install -r requirements.txt;
