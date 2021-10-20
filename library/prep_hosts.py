#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: prep_hosts

short_description: This modules generates Azure VM credentials.

version_added: "2.9"

description:
    - "This modules generates Azure VM credentials from account details."

options:
    name:
        count:
            - The amount of VM data sets to create.
        required: true

author:
    - Your Name (@yourhandle)
'''

EXAMPLES = '''
# Prepare two VMs
- name: Prepare VM metadata
  prep_hosts:
    count: 2
    register: vm_data
'''

RETURN = '''
instances:
    description: An array of created data sets with the properies "vm", "email" and "pw".
    type: array
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule

import os


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        count=dict(type='int', required=False),
        start=dict(type='int', required=False),
        end=dict(type='int', required=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        instances=[]
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    data = []

    vm_map = {}

    vm_count = -1
    if 'count' in module.params:
        vm_count = module.params['count']

    start = None
    end = None

    if 'start' in module.params:
        start = module.params['start']

    if 'end' in module.params:
        end = module.params['end']

    with open('files/user-accounts.csv') as f:
        i = 1
        for line in f.readlines():
            if line.strip() != '' and not line.startswith('Email'):
                params = line.strip().split(',')
                email = params[0]
                pw = params[1]
                data.append({
                    'vm': 'perf-vm-{}'.format(str(i)),
                    'email': email,
                    'pw': pw
                })
                i += 1

    if start and end:
        data = data[(start - 1):end]
    else:
        data = data[:vm_count]

    for vm_data_instance in data:
        vm_map[vm_data_instance['vm']] = {
            'email': vm_data_instance['email'],
            'pw': vm_data_instance['pw']
        }
    
    if i < vm_count:
        module.fail_json(msg='Not enough accounts available.', **result)

    result['instances'] = data
    result['vm_map'] = vm_map

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    #
    # We are only generating meta data, so no state changes occur.

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
