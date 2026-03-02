import os
import platform
import subprocess
import sys


def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")


def ping_target(target):
    param = "-n" if platform.system() == "Windows" else "-c"
    command = ["ping", param, "4", target]

    print(f"\nPinging {target}...\n")

    try:
        subprocess.run(command)
    except Exception as e:
        print(f"Error: {e}")


def show_help():
    print("""
Usage:
Select option 1
Then type:

pingm1 example.com

Example:
pingm1 google.com
""")


def main_menu():
    while True:
        print("""
==============================
        NetPingCLI v1.0
==============================
1 - Ping Target
2 - Help
3 - Clear Screen
4 - Exit
==============================
""")

        choice = input("Select option (1-4): ").strip()

        if choice == "1":
            user_input = input("Enter command: ").strip()

            if user_input.startswith("pingm1 "):
                parts = user_input.split(" ")

                if len(parts) == 2:
                    target = parts[1]
                    ping_target(target)
                else:
                    print("Invalid format. Example: pingm1 google.com")
            else:
                print("Unknown command. Use: pingm1 <target>")

        elif choice == "2":
            show_help()

        elif choice == "3":
            clear_screen()

        elif choice == "4":
            print("Exiting NetPingCLI...")
            sys.exit()

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    clear_screen()
    main_menu()