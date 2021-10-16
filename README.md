# Project
CSE-535 Distributed Systems
State Machine Replication using Diem-v4

### Python Version 
python : 3.7.12

### Setup guide
1. Download python. (preferably 3.7)
2. Create virtualenv of python=3.7 in your system
```
virtualenv -p=python3.7 env_name
```
3. Install python libraries using requirements.txt
```
pip install -r requirements.txt
```

### Execution Guide
1. Execute following command to run diem v4.
```
python -m da -f -m file_name.da
```
da : To run DistAlgo file (.da)
-f : Print logs on command line
-m : run this file as a python module

### Contributors guide
- Create a feature branch for working on any new feature.
- Remember to take a fresh pull of `master` branch before creating a new branch
- Raise a Pull request once the changes are done and tested

### System details
```
OS : Ubuntu 20.04 LTS
Python version : python 3.7.11
```

### References
1. [State Machine Replication : Diem-v4](https://developers.diem.com/docs/technical-papers/state-machine-replication-paper/)
2. [DistAlgo](https://github.com/DistAlgo/distalgo) 
