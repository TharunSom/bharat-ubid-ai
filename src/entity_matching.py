from rapidfuzz import fuzz

# Function to check similarity between two business names
def is_same_business(name1, name2):
    score = fuzz.token_sort_ratio(name1, name2)
    return score > 80  # threshold (you can tune this)

# Function to group duplicate businesses
def match_entities(df):
    groups = []
    visited = set()

    for i in range(len(df)):
        if i in visited:
            continue

        group = [i]

        for j in range(i + 1, len(df)):
            name1 = str(df['business_name'][i]).lower()
            name2 = str(df['business_name'][j]).lower()

            if is_same_business(name1, name2):
                group.append(j)
                visited.add(j)

        groups.append(group)

    return groups
