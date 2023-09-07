LR=2e-5
GRAD_STEPS=8
TRAIN_BS=2
VALID_BS=128
EPOCHS=-1
STEPS=30
WARMUP_STEPS=5
GPUS=0,1
GPU_COUNT=2
NODE_COUNT=1
NUM_WORKERS=32

TEMP=0.05
MARGIN=0.5

CODEGEN_DROPOUT_LAYERS=0
CODEGEN_DROPOUT_P=0.1

DATA_DIR="toy_data_preprocessed"
TRAIN_DIR="${DATA_DIR}/train"
VALID_DIR="${DATA_DIR}/valid"

export CUDA_HOME=/usr/local/cuda

options=(
   '--loss MLE_Only'
#   '--loss ContraCLMSeq --temperature $TEMP'
#   '--loss ContraCLMTok --temperature $TEMP'
#   '--loss ContraCLM --temperature $TEMP'
)

for ind in 0
do
   CL=$(eval echo ${options[$ind]})
   ### with retrieval data
   CUDA_VISIBLE_DEVICES=$GPUS python pl_trainer.py \
      --num_workers $NUM_WORKERS \
      --devices $GPU_COUNT \
      --accelerator gpu \
      --model_name Salesforce/codegen-6B-mono \
      --pad_token_id 50256 \
      --dropout_layers $CODEGEN_DROPOUT_LAYERS \
      --functional_dropout \
      --dropout_p 0.1 \
      --expt_prefix BigQuery_v3 \
      --default_root_dir /nobackup.2/yuhao/tmp/logs_store/deepspeed/ \
      --train_datadir $TRAIN_DIR \
      --valid_datadir $VALID_DIR \
      --log_dir ./logs/ \
      --seed 1234 \
      --lr $LR \
      --weight_decay 0.1 \
      --gradient_clip_val 1.0 \
      --max_steps $STEPS \
      --max_epochs $EPOCHS \
      --warmup_steps $WARMUP_STEPS \
      --train_batch_size $TRAIN_BS \
      --valid_batch_size $VALID_BS \
      --accumulate_grad_batches $GRAD_STEPS \
      --log_every_n_steps 5 \
      --save_step_frequency 50 \
      --val_check_interval 1 \
      --debug_cuda_mem \
      --use_deepspeed \
      --precision 16  \
      --ds_config stage3.json \
      $CL

   wait
done
