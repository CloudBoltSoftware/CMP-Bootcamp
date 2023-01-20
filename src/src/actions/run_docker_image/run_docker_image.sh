#!/bin/bash
docker run --restart=always -dp {{ port_mappings }} --name {{ name }} {{ extra_args }} {{ image }}

