import pandas as pd

chunks = pd.read_json("data/confusion-2014-03-02.json", lines=True, chunksize=10)
for c in chunks:
    print(c["choices"])
    break