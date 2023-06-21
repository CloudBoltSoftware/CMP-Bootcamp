#!/bin/bash

SERVICE="{{ SERVICE_NAME }}"
systemctl enable $SERVICE
systemctl start $SERVICE