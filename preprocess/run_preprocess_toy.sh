DATA_DIR="../toy_data_raw"
OUTPUT_DIR="../toy_data_preprocessed"
SEQ_LENGTH=512

python preprocess_toy.py \
    --data_dir $DATA_DIR \
    --output_dir $OUTPUT_DIR \
    --seed 0 \
    --test_and_valid_combined_size 0.04 \
    --seq_length $SEQ_LENGTH \
    --chars_per_tok 3.2 \
    --codegen_pad_token_id 50256
