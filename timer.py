import sys
import time
from datetime import timedelta
import curses


class TrainingTimer(object):
    """Ncurses boxing/cardio trainer timer"""

    def __init__(self, round_total=10, round_duration=60,
                 rest_round_duration=30):
        """
        Arguments:
        - `round_duration`: duration of a round in seconds
        - `total_round`: total amount of round
        - `rest_round_duration`: rest round duration in seconds
        """
        self._round_duration = round_duration
        self._round_total = round_total if round_total else 1
        self._rest_round_duration = rest_round_duration
        self.stdscr = None
        self.init_screen()  # We start ncurses
        self._RED = 1
        self._GREEN = 2

    def beep(self):
        """Performe a naive terminal beep"""
        sys.stdout.write("\a")

    def init_screen(self):
        """Initialise ncurses screen"""
        self.stdscr = curses.initscr()
        curses.start_color()
        # We set red color to 1
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        # We set green color to 2
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)

    def terminate_screen(self):
        """Restore terminal in his previous state"""
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def draw_timer(self, current_round, round_total,
                   timer_value, color_indice):
        """Draw timer screen using ncurses"""
        self.stdscr.addstr(0, 0, "round: %s, remaining: %s" %
                           (current_round, round_total - current_round))
        self.stdscr.addstr(12, 25, str(timer_value),
                           curses.color_pair(color_indice))
        self.stdscr.refresh()

    def round_timer(self, current_round, round_total, duration, color_indice):
        """Launch a timer for a given round.
        - `current_round`: the current round number
        - `round_total`: the last round number
        - `duration`: duration of round in second
        - `color_indice`: color of timer. self._GREEN or self._RED"""
        for second in xrange(duration, 0, -1):
                self.draw_timer(current_round,
                                round_total,
                                str(timedelta(seconds=second)),
                                color_indice)
                time.sleep(1)
        self.beep()

    def start_timers(self):
        """Run all rounds and rest rest rounds timer.
        Naive implementation."""
        for current_round in xrange(1, self._round_total + 1):
            self.round_timer(current_round,
                             self._round_total,
                             self._round_duration,
                             self._RED)
            if self._rest_round_duration:
                self.round_timer(current_round,
                                 self._round_total,
                                 self._rest_round_duration,
                                 self._GREEN)


if __name__ == '__main__':
    import argparse
    desc = ("Launch a cardio/boxing timer that can be use remotely.\n"
            "It uses terminal beep, and font size.\n"
            "Check your termial options to enable sound")
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-n', type=int, default=10, dest='nb_round',
                        help='Number of rounds')

    parser.add_argument('-l', type=int, default=60, dest='round_duration',
                        help='Lenght of rounds in seconds')

    parser.add_argument('-r', type=int, default=0, dest='rest_round_duration',
                        help='Lenght of rest rounds in seconds.\n'
                             'If not set no rest round will be launched')
    args = parser.parse_args()

    timer = TrainingTimer(args.nb_round, args.round_duration,
                          args.rest_round_duration)
    timer.start_timers()
    timer.terminate_screen()
