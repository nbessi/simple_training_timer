Simple cardio/boxing training timer
===================================

A simple cardio/boxing timer meant to be launched in terminal locally or remotely. Written in Python/Ncurses.

It uses terminal beep, and font size. Edit/create a terminal profile that fits your need. If font size it too big the script will crash. I personnaly use Menlo 38 font settings.

Usage
=====
```
python timer.py [-h] [-n NB_ROUND] [-l ROUND_DURATION] [-r REST_ROUND_DURATION]

optional arguments:
  -h, --help            show this help message and exit
  -n NB_ROUND           Number of rounds
  -l ROUND_DURATION     Lenght of rounds in seconds
  -r REST_ROUND_DURATION
                        Lenght of rest rounds in seconds. If not set no rest
                        round will be launched
```