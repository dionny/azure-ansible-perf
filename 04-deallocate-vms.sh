#!/bin/bash

set -e
set -x

cp perf.azure_rm.tmpl.yml perf.azure_rm.yml
sed -i -e "s/REPLACE_RESOURCE_GROUP/$1/g" perf.azure_rm.yml

ansible-playbook -f 10 -i perf.azure_rm.yml 04-deallocate-vms.yml --extra-vars '{"vm_password":"'"$VM_PASSWORD"'"}'
