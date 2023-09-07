import glob
import json
import os

all_files = glob.glob('**/*.py', recursive=True)
outdir = "toy_data_raw"
if not os.path.exists(outdir):
    os.makedirs(outdir)
# read all jsonl files and collect all data together tracking origin files
for filepath in all_files:
    origin = '_'.join(filepath.split('/')[-2:])
    print(origin)
    file_content = open(filepath, 'r').read()
    json.dump({'content': file_content}, open(os.path.join(outdir, origin + ".jsonl"), 'w'))