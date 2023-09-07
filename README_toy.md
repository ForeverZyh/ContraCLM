# This is the tutorial for running the toy examples

## 1. Install the package.
```bash
# create a new conda environment with python >= 3.8
conda create -n llm python=3.8

# install dependencies within the environment
conda activate llm
pip install -r requirements.txt
```

## 2. Load and inference the model.
Please see `load_codegen_350.py`

## 3. Query the OpenAI APIs.
Please see `query_api.py`

## 2. Prepare the data
```bash
# create the training data
python prepare_toy_raw.py

# tokenize the data
cd preprocess
./run_preprocess_toy.sh
cd ..

# finetune the 350M model
./runscripts/run_toy.sh

# finetune the 6B model
./runscripts/run_toy_large.sh
```