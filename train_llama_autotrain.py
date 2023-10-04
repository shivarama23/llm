!autotrain llm --train --project_name redactor-llm --model abhishek/llama-2-7b-hf-small-shards --data_path . --use_peft --use_int4 --learning_rate 2e-4 --train_batch_size 2 --num_train_epochs 3 --trainer sft


def extract_values(text):
    lines = text.split('\n')  # Split input text into lines
    result = []  # Initialize an empty list to store the output

    for line in lines:
        parts = line.split(':')  # Split each line into key and value
        if len(parts) == 2:
            key, values = parts[0].strip(), parts[1].strip()  # Extract key and values
            values = values.split(',')  # Split values by comma
            for value in values:
                result.append((value.strip(), key))  # Append tuples to the result list

    return result

# Example usage:
input_text = """
Name: K. V. Shivaramakrishna, Harish Salve
Age: 23, 24
Medical_history: Dizziness, something
"""

output = extract_values(input_text)
print(output)
