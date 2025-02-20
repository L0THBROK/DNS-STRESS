import os
import subprocess
import time
from termcolor import colored

# List of GitHub repositories to clone
repos = {
    "HULK": "https://github.com/adi-ace/HULK",
    "Slowloris": "https://github.com/gkbrk/slowloris",
    "LOIC": "https://github.com/NewEraCracker/LOIC",
    "DDosify": "https://github.com/chenyanming/ddosify",
    "Xerxes": "https://github.com/rofl0r/xerxes",
    "RUDY": "https://github.com/chrizster/rudy",
    "Aardvark": "https://github.com/alesgenova/aardvark",
    "GoldenEye": "https://github.com/jseidl/GoldenEye",
    "Hping3": "https://github.com/antirez/hping",
    "Scapy": "https://github.com/secdev/scapy"
}

def welcome_message():
    print(colored("==========================================", 'cyan', attrs=['bold']))
    print(colored("Welcome by Lothbrok9!", 'green', attrs=['bold']))
    print(colored("==========================================", 'cyan', attrs=['bold']))
    time.sleep(1)

def show_menu():
    print(colored("\nChoose an option to clone a repository:", 'yellow'))
    for i, repo in enumerate(repos.keys(), 1):
        print(colored(f"{i}. {repo}", 'green'))

def clone_repository(repo_name):
    try:
        repo_url = repos.get(repo_name)
        if repo_url:
            print(colored(f"\nCloning {repo_name} repository...", 'blue'))
            subprocess.check_call(["git", "clone", repo_url])  # Clone the repo using git
            print(colored(f"{repo_name} repository cloned successfully!", 'green'))
        else:
            print(colored(f"Repository {repo_name} not found!", 'red'))
    except subprocess.CalledProcessError:
        print(colored(f"Error cloning {repo_name}. Please check your internet connection and try again.", 'red'))

def handle_choice(choice):
    try:
        choice = int(choice)
        if choice < 1 or choice > len(repos):
            raise ValueError("Invalid choice! Please select a number from the menu.")
        
        repo_name = list(repos.keys())[choice - 1]  # Get the corresponding repo name
        clone_repository(repo_name)

    except ValueError as e:
        print(colored(f"Error: {str(e)}", 'red'))
        time.sleep(1)
    
    except Exception as e:
        print(colored(f"An unexpected error occurred: {str(e)}", 'red'))
        time.sleep(1)

def main():
    welcome_message()
    
    while True:
        show_menu()
        
        try:
            choice = input(colored("Enter the number to clone a repository (or 'exit' to quit): ", 'white')).strip()
            if choice.lower() == 'exit':
                print(colored("\nExiting the program...", 'red'))
                break
            handle_choice(choice)
        except Exception as e:
            print(colored(f"Error: {str(e)}", 'red'))
            time.sleep(1)

if __name__ == "__main__":
    main()
