# cs410-project

## Development

Install Anaconda.

```bash
conda create -n cs410
conda activate cs410
conda config --env --set subdir osx-64
conda install python=3.6.13
pip install metapy ir_datasets
```

```bash
pip install -r requirements.txt
```

```bash
python load_data.py
```

```bash
python search_eval.py
```
