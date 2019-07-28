### Systemd-test

This project was created to illustrate how to create a System.d daemon 
in Python that utilizes DBus for IPC/RPC by receiving messages from 
another System.d service and creating signals other DBus-aware software
can listen for. 

---
### Installation instructions:
- After changing to your selected directory on your machine:

```
git clone https://github.com/rbasn-us/systemd-test.git systemd-test
sudo pip install pydbus, csystemd
cd systemd-test/venv/systemd-test
```

- Make the systemd scripts being called executable:

```
chmod +x systemd_daemon.py
chmod +x systemd_test.py
```

- Modify the two .service files to point to your installation directory:  

systemd_daemon.service:
```
ExecStart=/CHANGE/TO/YOUR/INSTALL/DIRECTORY/systemd-test/venv/systemd-test/systemd_daemon.py start
ExecStop=/CHANGE/TO/YOUR/INSTALL/DIRECTORY/systemd-test/venv/systemd-test/systemd_daemon.py stop
```

systemd_test.service:

```
ExecStart=/CHANGE/TO/YOUR/INSTALL/DIRECTORY/systemd-test/venv/systemd-test/systemd_test.py start
ExecStop=/CHANGE/TO/YOUR/INSTALL/DIRECTORY/systemd-test/venv/systemd-test/systemd_test.py stop
```

- Move the files around to where they need to go:

```
mv systemd_daemon.service /etc/systemd/system/
mv systemd_test.service /etc/systemd/system/
mv us.rbasn.systemd.test.conf /etc/dbus-1/system.d/
```

- Reload systemd and start the services:

```
sudo systemctl daemon-reload
sudo systemctl start systemd_daemon
sudo systemctl start systemd_test
```

- And finally, run the signal listener to output to the command line 
when signals are being fired by the daemon:

```
python signal_listening.py
```