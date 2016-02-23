# Automation deployment for servers

## General

The script with ssh to server, pull code and run deploy bash scripts

## Requirements

fabric must be installed

How to install fabric

[Fabric](http://www.fabfile.org/)

## Usage

    fab load `server` deploy

    Eg: fab load staging deploy

## Brief explanation

    env.user = 'root' // this is ssh user for servers

    env.hosts = ['host-1', 'host-2'] // list of hosts

## Trobleshooting

TODO
