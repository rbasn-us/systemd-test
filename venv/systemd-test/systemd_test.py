#!/usr/bin/env python3
# systemd_test.py
# date: July 28, 2019
# author: Joe Rusbasan
# After being called from the systemd service, generates systemd notifications and sends messages to systemd_daemon.

import sys
import time
import pydbus
from gi.repository import GLib
from cysystemd.daemon import notify, Notification


def update_daemon(value):
    try:
        pydbus.SystemBus().get("us.rbasn.systemd.test").receive_signal(value)
    except GLib.Error:
        print("Failed to connect to signal.")


option = sys.argv[1]

if option == "start":
    counter = 0
    notify(Notification.READY)
    notify(Notification.STATUS, "Starting systemd_test...")
    while True:
        counter += 1
        notify(Notification.STATUS, "Notification #: %6s" % str(counter))
        update_daemon("Count: %+6s" % counter)
        time.sleep(5)

else:
    notify(Notification.STATUS, "Stopping systemd_test.")
    notify(Notification.STOPPING)
    # sys.exit(0)
