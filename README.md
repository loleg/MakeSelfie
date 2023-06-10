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

## Install OpenCV

If you have not yet installed [OpenCV](https://pypi.org/project/opencv-python/) and [hdf5](https://www.archlinux.org/packages/community/x86_64/hdf5/), do it. E.g. on Arch Linux:

`pacman -S opencv python-opencv hdf5`


## Run the Python program

Make sure you have Python 3.10+ and [Poetry](https://python-poetry.org/docs/) installed, then:

`poetry install`

Or use your virtual environment manager (venv etc.) of choice, e.g.:

```
pipenv shell
pip3 install -r requirements.txt
```

To get dependencies, and finally:

`python selfie.py`

To fire up the app!

## Set up your badge

Copy the `code.py` file to your MakeZurich badge.

Change the username to your account on https://now.makezurich.ch

Connect or reset the badge while your Python program is running to generate a selfie.


# License

Open source under the [MIT License](LICENSE)
