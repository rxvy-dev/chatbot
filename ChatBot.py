# ===============================================
#   ChatBot (written in Python)
# ===============================================
#   Author   : rxvy
#   Language : Python 3
#   Made for : Linux (uses fastfetch, date, clear, whoami)
#   Version  : 1.0
#   License  : free to use, edit, and share
#
#   What it does:
#     - Chats back using a big if / elif chain
#     - Answers PC, Linux, and package manager questions
#     - Runs a few system commands through subprocess
#     - Has easter eggs (sudo, rm -rf /, gentoo, etc.)
#
#   Note: it has 0 parameters, it's just if and elif.
#   Also available in C, see the c/ folder in this repo.
#
#   Run  : python3 ChatBot.py
#   Exit : Ctrl+C
# ===============================================

import subprocess

def menu():
   print("  _              _\n")    
   print(" /  |_   _. _|_ |_)  _ _|_\n")
   print(" |_ | | (_|  |_ |_) (_) |_ \n")
   print("\n")

def main():
   menu()
   while True:

    user = input("?:")

# main convos
    if 'hey' in user:
        print("HAYYY")

    elif 'hi' in user:
        print("HAYYY")

    elif user == 'C':
        print("AMAZING LANGUAGE")

    elif user == 'python':
        print("AMAZING LANGUAGE")

    elif 'stupid' in user:
        print("im zero paramenters what do u expect")

    elif 'linux' in user:
        print("aura")

    elif 'windows' in user:
        print("winslop")

    elif 'winslop' in user:
        print("winslop is so bad")

    elif 'smart' in user:
        print("nuh uh")

    elif 'microsoft' in user:
        print("Microslop*")

    elif 'yah' in user:
        print("NAH")

    elif 'nah' in user:
        print("YAH")

    elif 'yes' in user:
        print("no")

    elif user == 'no':
        print("yes")

    elif 'yep' in user:
        print("nope")

    elif 'nope' in user:
        print("yep")

    elif 'open source' in user:
        print("HOLY AURA")

    elif 'closed source' in user:
        print("-12382137128378273823782 aura...")

    elif 'joke' in user:
        print("Deleting the french language now.")

    elif 'sudo' in user:
        print("you are not in the sudoers file. this incident will be reported.")

    elif 'rm -rf /' in user:
        print("Sorry you do not have permission to do this.")

    elif 'gentoo' in user:
        print("SEE YOU IN 2 DAYS (compiling...)")

    elif 'fastfetch' in user:
        subprocess.run(['fastfetch'])

    elif 'date' in user:
        subprocess.run(['date'])

    elif 'clear' in user:
        subprocess.run(['clear'])

    elif 'whoami' in user:
        subprocess.run(['whoami'])

    elif 'computer' in user:
        print("A computer (also known as a PC) is an electronic machine that stores, processes, and displays information by following programmed instructions")

    elif 'ram' in user:
        print("RAM (Random Access Memory) is your computer's short-term memory that temporarily holds active data and programs for fast access by the processor")

    elif 'hhd' in user:
        print("An HHD (Hybrid Hard Drive) is a storage device that combines a traditional spinning hard disk drive (HDD) with a small amount of flash memory (SSD cache)")

    elif 'ssd' in user:
        print("An SSD (Solid-State Drive) is a modern data storage device that uses flash memory chips to save and access data instantly without any moving parts")

    elif 'cpu' in user:
        print("The CPU (Central Processing Unit) is the brain of the computer that executes instructions, performs calculations, and manages data flow.")

    elif 'gpu' in user:
        print("The GPU (Graphics Processing Unit) is a specialized processor designed to handle visual rendering, 3D graphics, images, and video processing.")

    elif 'motherboard' in user:
        print("The motherboard is the main printed circuit board that physically connects and allows communication between the CPU, RAM, storage, and all other components")    

    elif 'power supply' in user:
        print("The PSU (Power Supply Unit) converts electrical power from an outlet into usable, regulated voltage for all the internal components of the computer.")

    elif 'hdd' in user:
        print("An HDD (Hard Disk Drive) is a legacy magnetic storage device that uses mechanical spinning platters and a moving read/write head to read data.")

    elif 'operating system' in user:
        print("An operating system is the master control software that manages all hardware resources and applications on a computer.")

    elif 'ghz' in user:
        print("Gigahertz (GHz) measures a CPU's clock speed, indicating how many billions of calculations the processor can perform per second.")

    elif 'story' in user:
        print("Hey, thanks for wanting to know my story, i started my coding adventure with python and i coded multiple chatbots in that it was fun and now im on C and its WAY funner! anyway have fun with this code!!!")

    elif 'pacman' in user:
        print("The AUR (Arch User Repository) is a community-driven repository where users upload package build scripts (PKGBUILDs) allowing anyone to compile and install software not found in the official repositories.")

    elif 'emerge' in user:
        print("Emerge is the core package management interface for Gentoo's Portage system, which downloads source code, applies local optimization flags, and compiles packages natively on your machine")

    elif 'flatpak' in user:
        print("Flatpak is a universal sandboxed package deployment utility designed to package and distribute desktop applications across any Linux distribution without relying on system-level runtimes")    

    elif 'apt' in user:
        print("APT (Advanced Package Tool) is the default package manager for Debian, Ubuntu, and their derivatives, utilizing pre-compiled .deb binaries and handling dependencies automatically.")

    elif 'xbps' in user:
        print("XBPS (X Binary Package System) is the fast, native package manager for Void Linux, written from scratch to handle package installations, removals, and dependency resolution using simple metadata")

    elif 'dnf' in user:
        print("DNF (Dandified YUM) is the next-generation package manager for RPM-based distributions like Fedora and Red Hat Enterprise Linux, known for strict dependency tracking and clean metadata management.")

    elif 'wayland' in user:
        print("Wayland and X11 (Xorg) are display server protocols that enable the operating system to communicate with your graphics hardware so applications can draw windows and interface elements on your screen")

    elif 'kernel' in user:
        print("The kernel is the core program of an operating system that holds absolute control over everything in the system, acting as the primary bridge between hardware components and running software applications")

    elif 'root' in user:
        print("Root is the conventional name of the administrative user account on Unix-like operating systems, possessing universal read, write, and execute permissions across the entire file system")

    elif 'nixos' in user:
        print("NixOS is a declarative Linux distribution built on the Nix package manager where the entire system configuration, including packages, services, and user settings, is defined inside a single monolithic configuration file (configuration.nix)")

    elif 'grub' in user:
        print("GRUB (Grand Unified Bootloader) is the primary program that starts your computer and loads the Linux operating system kernel into memory")

    elif 'gnu' in user:
        print("GNU is a free software operating system and project created to give computer users complete freedom over their software")

    else:
        print("you like " + user + " thats cool too!")

main()