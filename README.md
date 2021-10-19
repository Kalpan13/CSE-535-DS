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
python -m da -f -m src.orig num_replicas num_clients num_request f fail_idx logger_file_name > Test0.txt
```

da : To run DistAlgo file (.da), 

-f : Print logs on command line,

-m : run this file as a python module

fail_idx : node_id to be stopped 



### System details
```
Operating System Used: Linux 20.0.4 LTS
Type of host: Laptop
Python Implementation: CPython
Python version: 3.7
```

###  Workload Generation
- Client Workload Generation:
- Every client contains a list of transactions that are broadcasted to each server.
- Clients do not need wait explicitly between two successive requests.
- If clients want n requests to be committed in ledger, they need to send n+2 commands. - - The last two commands are no-op commands.

### File Structure
- Code for clients and replicas is present in only one file. Following is the path of the file: orig.da
- The file structure.py contains definitions of the following classes: transaction, proposal message, QC, vote message, etc. Path of the file: 
src/structures.py
- logs folder contains logs of test cases
- ledger_outputs contains tree views of ledgers. Writing output to the file is sometimes causing timeout. Hence, command line outputs are redirected to .txt

### Line of Codes : ~ 500
### No of Comments : 50
### No of lines for logging : 37
### References
1. [State Machine Replication : Diem-v4](https://developers.diem.com/docs/technical-papers/state-machine-replication-paper/)
2. [DistAlgo](https://github.com/DistAlgo/distalgo) 


### Known bugs
1. System may behave abruptly and may end up adding redundant transactions in ledger for send_rate_failure > 0.2
2. For 2 continuous failures of rounds, one/two extra commands may get committed in the ledger. 
3. For more than clients > 3 and commands > 6 (total 18 commands), system may display random behaviour and may not end all the process because of the timeout configuration issues. 


### Contribution
1. Basic Code writeup: Swetang + Kalpan
2. Timeout Implementation : Kalpan
3. Digital Signatures : Swetang
4. Project Report : Swetang
5. Test case generation : Kalpan



### Contributors guide
- Create a feature branch for working on any new feature.
- Remember to take a fresh pull of `master` branch before creating a new branch
- Raise a Pull request once the changes are done and tested
