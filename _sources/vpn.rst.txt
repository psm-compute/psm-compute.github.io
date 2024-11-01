VPN tips
========

To automaticaly connect to the UGA VPN, you can
create a bash script named `vpn-connect.sh` and
containing the following information:

.. code:: bash

    #!/bin/bash

    # Define VPN server, username, password, and group
    VPN_SERVER="vpn.grenet.fr"
    VPN_USER="your-username-here"
    VPN_PASSWORD="your-password-here"
    VPN_GROUP="Personnels de l' UGA"

    # Path to the log file
    OCLOG="$HOME/vpn_connection.log"

    echo "Connecting to VPN at $VPN_SERVER with username $VPN_USER"
    echo "You may be prompted for your sudo password if necessary..."

    # Use openconnect with protocol, group, and password provided via echo
    echo "$VPN_PASSWORD" | sudo openconnect --protocol=anyconnect --authgroup="$VPN_GROUP" --user="$VPN_USER" "$VPN_SERVER" --passwd-on-stdin | tee -a "$OCLOG"

    echo "VPN connection established. Logs can be found at $OCLOG"

WARNING
-------

You don't have to save your password in `vpn-connect.sh`.
If you leave the `VPN_PASSWORD` blank, you will be prompted
to type your password. If you choose to write your password in
the file, you can still protect the file using:

.. code:: bash

    sudo chown root:root vpn-connect.sh
    sudo chmod 700 vpn-connect.sh