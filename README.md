# Azure + Ansible for Performance Testing

## Environment Setup

1. Modify the `credentials` file with your Azure credential information.

```
[default]
subscription_id=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
client_id=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
secret=xxxxxxxxxxxxxxxxx
tenant=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

2. Copy your credentials to your $HOME/.azure directory.

```
cp credentials $HOME/.azure/credentials
```

3. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

4. Setup your Python environment, and install Ansible by running the following in a terminal:

```
conda create --name azurepy python=3.9.5
conda activate azurepy
conda install -c conda-forge ansible
conda deactivate
conda activate azurepy
pip install 'ansible[azure]'
curl -O https://raw.githubusercontent.com/ansible-collections/azure/dev/requirements-azure.txt
pip install -r requirements-azure.txt
pip install pywinrm
export PYTHONPATH=$PYTHONPATH:$CONDA_PREFIX/lib/python3.9/site-packages
```

## Automating VM Creation

1. Set your VM Password (this is the password used to log in to the created VMs).

```
export VM_PASSWORD=SuperSecretPassword
```

2. You can use the `01-create-vms.sh` script to create VMs:

```bash
$ ./01-create-vms.sh <resource-group> <region> <num_vms>
```

For example, to deploy 10 VMs to the resource group `perf-rg-1`:

```bash
$ ./01-create-vms.sh perf-rg-1 eastus 10
```

## Listing VMs

1. To list VMs across all resource groups, execute the following script:

```
./02-list-vms.sh
```

2. Alternatively, to list VMs belonging to a specific resource group:

```
./02-list-vms.sh <resource-group>
```

## Automating Software Installation

1. Set your VM Password (this is the password used to log in to the created VMs).

```
export VM_PASSWORD=SuperSecretPassword
```

2. To install software for VMs across all resource groups, execute the following script:

```
./03-install-sw.sh
```

3. Alternatively, to install software on VMs belonging to a specific resource group:

```
./03-install-sw.sh <resource-group>
```

## Deallocating VMs

1. Set your VM Password (this is the password used to log in to the created VMs).

```
export VM_PASSWORD=SuperSecretPassword
```

2. To deallocate (stop) VMs across all resource groups, execute the following script:

```
./04-deallocate-vms.sh
```

3. Alternatively, to deallocate (stop) VMs belonging to a specific resource group:

```
./04-deallocate-vms.sh <resource-group>
```

## Deleting VMs

1. Set your VM Password (this is the password used to log in to the created VMs).

```
export VM_PASSWORD=SuperSecretPassword
```

2. To delete VMs across all resource groups, execute the following script:

```
./05-delete-vms.sh
```

3. Alternatively, to delete VMs belonging to a specific resource group:

```
./05-delete-vms.sh <resource-group>
```

## Remote Desktop

You may use RDP software to remote desktop into one of the created VMs. The `username` is `azureuser`. For the password, use the same value you used throughout this README.