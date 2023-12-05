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

### Choose a ranker

Choose a ranker by providing another argument to the command, like:

```bash
python search_eval.py 1
```

**Mapping**:

-   0 (or empty): OkapiBM25(k1=5,b=0.75,k3=1.5),
-   1: metapy.index.DirichletPrior(0.75),
-   2: metapy.index.JelinekMercer(),
-   3: metapy.index.PivotedLength(),
