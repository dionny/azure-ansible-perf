#!/bin/bash

set -e
set -x

cp perf.azure_rm.tmpl.yml perf.azure_rm.yml
sed -i -e "s/REPLACE_RESOURCE_GROUP/$1/g" perf.azure_rm.yml

ansible-playbook -f 50 -i perf.azure_rm.yml 01-create-vms.yml --extra-vars '{"count":"'"$3"'","vm_password":"'"$VM_PASSWORD"'", "azure_rg":"'"$1"'", "azure_location":"'"$2"'"}'