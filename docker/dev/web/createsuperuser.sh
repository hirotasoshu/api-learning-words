#!/bin/bash
#!/bin/bash

# check who owns the working directory
USER_ID=$(stat -c "%u" $PWD)

# set the web run uid to the user id we just retrieved
WEB_RUN_UID=${WEB_RUN_UID:=${USER_ID}}
WEB_RUN_USER=${WEB_RUN_USER:=user}
WEB_RUN_GROUP=${WEB_RUN_GROUP:=user}

# test to see if the user already exists
WEB_RUN_USER_TEST=$(grep "[a-zA-Z0-9\-\_]*:[a-zA-Z]:${WEB_RUN_UID}:" /etc/passwd)


# Update the user to the configured UID and group
if [ -n "${WEB_RUN_USER_TEST}" ]; then
    echo "Update user '$WEB_RUN_USER'"

    usermod -l ${WEB_RUN_USER} $(id -un ${WEB_RUN_UID})
    usermod -u $WEB_RUN_UID -g $WEB_RUN_GROUP $WEB_RUN_USER

# Else create the user with the configured UID and group
else
    echo "Create user '$WEB_RUN_USER'"

    # Create the user with the corresponding group
    mkdir /home/$WEB_RUN_USER
    groupadd $WEB_RUN_GROUP
    useradd -u $WEB_RUN_UID -g $WEB_RUN_GROUP -d /home/$WEB_RUN_USER $WEB_RUN_USER
    chown $WEB_RUN_USER:$WEB_RUN_GROUP /home/$WEB_RUN_USER
fi

export HOME=/home/$WEB_RUN_USER

echo 'Creating super user'

exec su -p ${WEB_RUN_USER} /bin/bash -c "python manage.py createsuperuser"