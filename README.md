# ChatBot

A tiny terminal chatbot written twice: once in **C** and once in **Python**.

Made by **rxvy**.

```
  _              _
 /  |_   _. _|_ |_)  _ _|_
 |_ | | (_|  |_ |_) (_) |_

?:hdd
Generating
An HDD (Hard Disk Drive) is a legacy magnetic storage device that uses mechanical spinning platters and a moving read/write head to read data.
```

## My story

I started my coding adventure with **Python**, and I built multiple chatbots in it. It was fun, and it's where I learned how to make a program talk back.

Then I moved on to **C**. This chatbot is my first C project, and it's way more fun. I wrote it on Auxo Linux, an Arch-based distro, which is why it's built around `pacman` and full of Linux jokes.

Once the C version worked, I went back to where I started and made a **Python** version too, so both live in this repo side by side. Same bot, two languages, and a good way to see what changed between my first language and my newest one.

If you want to hear it from the bot itself, run it and type `story`.

## Files

| File | Language | What it is |
|------|----------|------------|
| `ChatBot.c` | C | The original version |
| `ChatBot.py` | Python 3 | The Python port |

## Run it

**C**

```bash
gcc ChatBot.c -o chatbot
./chatbot
```

**Python**

```bash
python3 ChatBot.py
```

## What it can do

- **Chat:** say `hey`, insult it, or argue about Windows vs Linux
- **Facts:** PC hardware (`cpu`, `ram`, `ssd`, `motherboard`, ...) and Linux stuff (`pacman`, `aur`, `nixos`, `grub`, `wayland`, ...)
- **Package managers:** `pacman`, `apt`, `dnf`, `xbps`, `emerge`, `flatpak`
- **System commands:** `fastfetch`, `date`, `clear`, `whoami`
- **Easter eggs:** `sudo`, `rm -rf /`, `gentoo`, `open source`, `joke`, and more
- **Story:** type `story` to hear how this project started
- **Exit:** type `bye` or `quit` (C version)

## Requirements

- **Linux.** Both versions call Linux commands, and the C version uses `unistd.h`, so it won't build on plain Windows.
- **gcc** for the C version, **Python 3** for the Python version.
- **fastfetch** for the `fastfetch` command. If it's missing, the C version tries to install it with `sudo pacman -S fastfetch`, because it was built for Arch-based distros.

## Quirks

The bot matches words *anywhere* inside what you type, so it sometimes answers the wrong thing. For example, a word that contains `no` inside it can get a reply meant for `no`. That's part of the charm, and also on the to-do list.

## Ideas for later

- A `help` command
- Random replies
- A `teach` command so it can learn new answers
- Case-insensitive matching

## License

Free to use, edit, and share.
