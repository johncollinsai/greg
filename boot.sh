#!/bin/bash
# this script is used to boot a Docker container
# see https://github.com/miguelgrinberg/microblog/blob/main/boot.sh

source venv/bin/activate

while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

flask translate compile
# following https://github.com/miguelgrinberg/microblog/blob/main/boot.sh
# exec gunicorn -b :5000 --access-logfile - --error-logfile - johncollins:app

# following https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/hello-app/Dockerfile
exec gunicorn -b :8080 --access-logfile - --error-logfile - johncollins:app
