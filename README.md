# rgate-proxy
Proxy Server for Rgate

## PreRequisites
 
* Install python 3 on your machine : https://www.python.org/downloads/


 
## Creating aliases for running the code

Create the aliases for deployment,running and stopping rgate. RGate has a bug with aboslute paths. so please run them by changing the directory to the src folder of the cloned repo.

- ``` alias rgate-deploy="pytest --cov=../src/ ../tests -k test_deploy_rgate" ```
- ``` alias rgate-run="python3 rgate_proxy.py" ```
- ``` alias rgate-delete="pytest --cov=../src/ ../tests -k test_stop_rgate ```


## Steps for running RGate

### Deploying RGate :

- `cd tests`
-  `rgate-deploy`

### Running RGate :

- `cd src`
-  `rgate-deploy`

### Stopping RGate :

- `cd tests`
-  `rgate-delete`


### Validating RGate :

Without making Changes to hosts file

- `curl -H “Host: rgate” http://localhost:8080/api/payments/index.html` 


## Bugs/To-do's

- Change the working directory of rgate from src. Use absolute path instead of relative paths
- Expose the default port to be configurable from port 80 to a command line argument


