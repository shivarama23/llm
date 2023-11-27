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
