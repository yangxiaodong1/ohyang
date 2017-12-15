#!/bin/bash

supervisorctl -c /etc/supervisor/supervisord.conf stop ohho
sleep 1
supervisorctl -c /etc/supervisor/supervisord.conf start ohho

