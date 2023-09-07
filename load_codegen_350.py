from transformers import (AutoConfig, AutoModelForCausalLM, AutoTokenizer)
import torch

# model_name = "Salesforce/codegen-350M-mono"
model_name = "bigcode/starcoder"
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("tokenizer", tokenizer)
mod_config = AutoConfig.from_pretrained(model_name)
print("mod_config", mod_config)
model = AutoModelForCausalLM.from_pretrained(model_name, config=mod_config, cache_dir="/nobackup.2/yuhao/tmp",
                                             torch_dtype=torch.float16, device_map="auto")
device = torch.device("cuda")
# model = model.to(device)
model.eval()

with torch.no_grad():
    while True:
        input_str = input("Press any key to continue...")
        if len(input_str) == 0:
            continue
        input_ids = tokenizer(
            input_str).input_ids  # be careful, some tokenizer will add special tokens in the beginning
        print(input_str, input_ids)
        input_ids = torch.tensor(input_ids, dtype=torch.long).unsqueeze(0).to(device)
        ret = model.generate(input_ids, do_sample=True, max_length=100, top_k=50, top_p=0.95, temperature=0.8,
                             num_return_sequences=5)
        print(ret.shape)
        for i in range(ret.shape[0]):
            print("Sample", i, ":")
            print(tokenizer.decode(ret[i].tolist()))
