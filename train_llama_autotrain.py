!autotrain llm --train --project_name redactor-llm --model abhishek/llama-2-7b-hf-small-shards --data_path . --use_peft --use_int4 --learning_rate 2e-4 --train_batch_size 2 --num_train_epochs 3 --trainer sft