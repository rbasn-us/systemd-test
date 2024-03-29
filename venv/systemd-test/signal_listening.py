#!/usr/bin/env python3
# signal_listening.py
# date: July 28, 2019
# author: Joe Rusbasan
# Listen for signals emitted by systemd_daemon.py

from pydbus.generic import signal
from pydbus import SystemBus
from gi.repository import GLib

loop = GLib.MainLoop()
signal_filter = "/us/rbasn/systemd/test"


def signal_heard(*args):
    # Uncomment the following if you need to view all info generated by signal emissions:
    # print("Message: ", args)
    print(str(args[4][0]))


if __name__ == "__main__":
    print(SystemBus().subscribe(object=sysd_filter1, signal_fired=signal_heard))
    loop.run()
