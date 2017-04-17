# automated-arancino

automated-arancino is a lightweight analysis framework to automate malware analyses on a virtualized environment.
We developed automated-arancino to automatically perform experiments on [Arancino](https://github.com/necst/arancino).

## Install

To install automated-arancino run:

```
install.sh
```

Edit `config/general.py` and run `agent/mbare.py` inside the VMs.

## Run

automated-arancino is composed by four components:

* The agent, which has to be executed inside the VMs.
```
	python mbare.py
```

* The analysis manager.
```
	python automated-arancino.py
```

* The log-server, which stores the logs received from the VMs.
```
	python log-server.py
```

* The submitter, which watches a folder and submits tasks for the created files.
```
	python submitter.py
```

You can also submit a sample by running:
```
	python submit.py <sample_path>
```
