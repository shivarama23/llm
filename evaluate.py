def calculate_metrics(ground_truth_list, model_output_list):
    # Function to check overlap between two positions
    def check_overlap(pos1, pos2):
        overlap = min(pos1[1], pos2[1]) - max(pos1[0], pos2[0])
        return overlap / (pos1[1] - pos1[0]) >= 0.9 or overlap / (pos2[1] - pos2[0]) >= 0.9
    
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    
    # Ground truth entities compared with model output
    for entity in ground_truth_list:
        if entity in model_output_list:
            true_positives += 1
        else:
            found_overlap = False
            for predicted_entity in model_output_list:
                if entity[1:] == predicted_entity[1:] and check_overlap(entity[2:], predicted_entity[2:]):
                    found_overlap = True
                    break
            if found_overlap:
                true_positives += 1
            else:
                false_negatives += 1
    
    # Model output entities compared with ground truth
    for entity in model_output_list:
        if entity not in ground_truth_list:
            found_overlap = False
            for true_entity in ground_truth_list:
                if entity[1:] == true_entity[1:] and check_overlap(entity[2:], true_entity[2:]):
                    found_overlap = True
                    break
            if not found_overlap:
                false_positives += 1
    
    return true_positives, false_positives, true_negatives, false_negatives

# Example usage:
ground_truth_list = [('shiva', 'NAME', 3, 8), ('Nagpur', 'CITY', 9, 15), ('Hyderabad', 'CITY', 12, 21)]
model_output_list = [('shiva', 'NAME', 3, 8), ('Nagpur', 'CITY', 9, 15)]

TP, FP, TN, FN = calculate_metrics(ground_truth_list, model_output_list)
print("True Positives:", TP)
print("False Positives:", FP)
print("True Negatives:", TN)
print("False Negatives:", FN)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calculate_overlap(start1, end1, start2, end2):
    # Calculate the overlapping range
    overlap = max(0, min(end1, end2) - max(start1, start2))
    # Calculate the total range covered by both spans
    total_range = max(end1, end2) - min(start1, start2)
    # Calculate the percentage overlap
    return (overlap / total_range) * 100

def compare_entities(ground_truth, model_output):
    metrics = {'TP': [], 'FP': [], 'TN': [], 'FN': []}
    model_output_checked = []

    for gt_entity in ground_truth:
        match_found = False
        for mo_entity in model_output:
            if gt_entity[0] == mo_entity[0] and calculate_overlap(gt_entity[2], gt_entity[3], mo_entity[2], mo_entity[3]) >= 90:
                metrics['TP'].append(gt_entity)
                model_output_checked.append(mo_entity)
                match_found = True
                break
        if not match_found:
            metrics['FN'].append(gt_entity)

    for mo_entity in model_output:
        if mo_entity not in model_output_checked:
            metrics['FP'].append(mo_entity)

    # Assuming True Negatives are not directly identifiable in this context
    return metrics

def update_master_metrics(master_metrics, new_metrics):
    for metric in ['TP', 'FP', 'FN']:
        for entity in new_metrics[metric]:
            entity_type = entity[1]
            master_metrics[entity_type].setdefault(metric, 0)
            master_metrics[entity_type][metric] += 1
    return master_metrics

# Example Usage
ground_truth_list = [('Rama', 'NAME', 3, 8), ('Raipur', 'CITY', 9, 15)]
model_output_list = [('Rama', 'NAME', 3, 8), ('Raipur', 'CITY', 9, 15), ('Hyderabad', 'CITY', 12, 21)]

# Initialize master metrics dictionary
master_metrics = {'NAME': {}, 'CITY': {}}

# Compare entities
metrics = compare_entities(ground_truth_list, model_output_list)
print(metrics)
# Update master metrics
master_metrics = update_master_metrics(master_metrics, metrics)
print(master_metrics)

