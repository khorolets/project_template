#!/usr/bin/env bash

if [ ! $1 ]; then
    echo 'No command'
    exit 0
fi

ROOT=pwd
DOMAIN=$(awk -F "=" '/DOMAIN/{print $2}' config.ini)
PRJ_NAME=$(awk -F "=" '/NAME/{print $2}' config.ini)

if [ ! $MODE ]; then
    MODE="development";
fi

echo $MODE

function bootstrap_configs {
    if [ ! -d "conf/conf_tpl" ]; then
        echo '1111';
    fi;
}

echo $0 $1

if [ $1 == "configurate" ]; then
    echo "iiiiiii"
elif [ $1 == "test2" ]; then
    echo "222222"
fi

bootstrap_configs $ENVIRON
