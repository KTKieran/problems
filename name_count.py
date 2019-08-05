name_list = ['brian', 'daniel', 'kate', 'kevin', 'lola', 'brian', 'daniel', 'kate']

def name_counts_list(list_input):
    unique_names = []
    name_counts = []
    for each_name in list_input:
        if each_name in unique_names:
            for idx, na in enumerate (unique_names):
                if na == each_name:
                    name_counts[idx] += 1
        else:
            unique_names.append(each_name)
            name_counts.append(1)

    return unique_names, name_counts

def name_counts_dict(list_input):
    """
    Occurance count of each name in the list
    """

    # Adds each name to the counts_dict and if there's a corresponding name added to the counts_dict,
    # it adds one to the name
    counts_dict = {}
    for each_name in list_input:
        if each_name in counts_dict:
            counts_dict[each_name] += 1
        else:
            counts_dict [each_name] = 1

    return counts_dict



print(name_counts_list(name_list))
print(name_counts_dict(name_list))