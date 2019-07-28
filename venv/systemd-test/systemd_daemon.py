#!/usr/bin/env python3
# systemd_daemon.py
# date: July 28, 2019
# author: Joe Rusbasan
# Systemd initiated daemon that listens for messages from systemd_test.py and then emits a signal with the same
# information that was received.

from pydbus.generic import signal
from pydbus import SystemBus
import sys
from gi.repository import GLib


class SystemdTestDaemon(object):
    """
        <node>
            <interface name='us.rbasn.systemd.test'>
                <signal name='signalReceived'>
                    <arg type='s' name='value' direction='out'/>
                </signal>
                <method name='receive_signal'>
                    <arg type='s' name='response' direction='in'/>
                </method>
                <method name='quit'/>
            </interface>
        </node>
    """
    signalReceived = signal()

    def __init__(self):
        pass

    def receive_signal(self, value):
        """adds a drive to the list to ensure its toggle value and other information can be maintained"""
        self.signalReceived(value)

    def quit(self):
        """removes this object from the DBUS connection and exits"""
        loop.quit()


bus = SystemBus()
loop = GLib.MainLoop()
option = ""
if len(sys.argv) > 1:
    option = sys.argv[1]

if option == "start":
    try:
        bus.publish("us.rbasn.systemd.test", SystemdTestDaemon())
        loop.run()
    except GLib.Error as e:
        print(str(e))

else:
    try:
        bus.get("us.rbasn.systemd.test").quit()
    except GLib.Error as e:
        loop.quit()
