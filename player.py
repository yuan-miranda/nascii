import sys
import os
import time

FILE = None

def clear_console():
    if sys.platform.startswith('win'):
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main():
    global FILE
    if len(sys.argv) > 1:
        FILE = sys.argv[1]
    elif FILE is None:
        files = os.listdir("output")
        if not files:
            return print("No files found in /output directory.")
        
        for i, file in enumerate(files):
            print(f"{i}: {file}")
        
        try:
            choice = int(input("> "))
            if choice < 0 or choice >= len(files):
                raise ValueError()
            time.sleep(0.5)
            FILE = files[choice]
        except ValueError:
            return print(f"Invalid or out of range. Selection must be between 0 and {len(files) - 1}.")

    
    if not os.path.exists(f"media/{FILE}"):
        return print(f"{FILE} does not exist.")

    file_name = os.path.splitext(FILE)[0]
    FILE = os.path.join("output", file_name, f"{file_name}.txt")

    with open(FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line == "END\n":
                time.sleep(0.03)
                clear_console()
                continue

            print(line, end="")

if __name__ == "__main__":
    main()