#!/bin/bash

set -e
set -x

cp perf.azure_rm.tmpl.yml perf.azure_rm.yml
sed -i -e "s/REPLACE_RESOURCE_GROUP/$1/g" perf.azure_rm.yml

# Retrieves IPs and names of the VMs without contacting them.
ansible azure -i perf.azure_rm.yml -m debug -a "msg={{ansible_host}}"
