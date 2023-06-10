MakeSelfie
---

A MakeZurich 2023 hackathon project to explore ideas with embedded hardware and quantified self.

See https://now.makezurich.ch/project/89

# Installation

You need to have tkinter on your system:

In Arch, Tk is available in the Arch repository. You don't need aur for this, just type on the terminal:

`sudo pacman -S tk`

If you are on a Debian, Ubuntu or another Debian-based distro, just type on the terminal:

`sudo apt-get install tk`

On Fedora:

`sudo dnf install tk`

## Run the Python program

Make sure you have Python 3.10+ and Poetry installed, then:

`poetry install`

To get dependencies, and finally:

`python selfie.py`

## Set up your badge

Copy the `code.py` file to your MakeZurich badge.

Change the username to your account on https://now.makezurich.ch

Connect or reset the badge while your Python program is running to generate a selfie.

