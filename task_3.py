import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def print_directory_structure(path, indent=""):
    path = Path(path)

    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + f"📂 {item.name}" + Style.RESET_ALL)
            print_directory_structure(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + f"📜 {item.name}" + Style.RESET_ALL)


def main():
    if len(sys.argv) < 2:
        print("Please provide a directory path.")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print("The path does not exist.")
        return

    if not directory_path.is_dir():
        print("The path is not a directory.")
        return

    print(Fore.YELLOW + f"📦 {directory_path.name}" + Style.RESET_ALL)
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()