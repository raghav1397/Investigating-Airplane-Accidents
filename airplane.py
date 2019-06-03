aviation_list = []
aviation_data = []

with open('AviationData.txt', 'r') as file:
    for line in file:
        aviation_data.append(line)
        text = line.split('|')
        words = []
        for word in text:
            word = word.strip()
            words.append(word)
        aviation_list.append(words)

print(aviation_data[1]) # 0th row contains the headers
        
print(aviation_list[1])

def linear_search(code):
    lax_code = []    
    for row in aviation_list:
        for item in row:
            if item == code:
                lax_code.append(row)
    return lax_code


lin_search = linear_search('LAX94LA336')

print(lin_search[0])

def dictionary(l):
    # Clean input and create a list of keys for a dictionary    
    not_yet_keys = l[0].split('|')
    keys = []
    for key in not_yet_keys:
        key = key.strip()
        keys.append(key)
    
    # Get the values for the keys
    values = []
    for n in range(1, len(l)):
        not_yet_values = l[n].split('|')
        clean_values = []
        for value in not_yet_values:
            value = value.strip()
            clean_values.append(value)
        values.append(clean_values)
     
    # Pair the values to the keys
    aviation_dict_list = []
    for y in range(0, len(values)):
        paired = {}
        for x in range(0, len(keys)):        
            paired[keys[x]] = values[y][x]
        aviation_dict_list.append(paired)    
    return aviation_dict_list
        

        
aviation_dict_list = dictionary(aviation_data)
aviation_dict_list[1]

def dict_search(dict_list, target):
    lax_dict = []
    for x in range(0, len(dict_list)):
        for value in dict_list[x].values():
            if value == target:
                lax_dict.append(dict_list[x])
    return lax_dict


lax_dict = dict_search(aviation_dict_list, "LAX94LA336")

lax_dict[0]

from collections import Counter

def most_state_accidents(data):
    state_accidents = []
    for x in range(0, len(data)):
        state_accidents.append(data[x]['Location'][-2:])
    state_count = Counter(state_accidents)
    return state_accidents, state_count.most_common(5)

state_accidents, accident_prone_states = most_state_accidents(aviation_dict_list)

accident_prone_states

def worst_month_accidents(data):
    months = []
    change_month = {"01":"January",
                    "02":"February",
                    "03":"March",
                    "04":"April",
                    "05":"May",
                    "06":"June",
                    "07":"July",
                    "08":"August",
                    "09":"September",
                    "10":"October",
                    "11":"November",
                    "12":"December"}
    
    for x in range(0, len(data)):
        month = data[x]['Event Date'][0:2]
        try:
            month = change_month[month]
        except KeyError:
            month = data[x]['Event Id'][4:6]
            month = change_month[month]
        if data[x]['Event Date'] != '':
            year = data[x]['Event Date'][-4:]
        else:
            year = data[x]['Event Id'][0:4]
        months.append(month + ' ' + year)
        
    worst_months = Counter(months)
    return worst_months, worst_months.most_common(3)

month_count_accidents, worst_3_months_acc = worst_month_accidents(aviation_dict_list)

worst_3_months_acc

def worst_month_injuries(data):
    injuries_by_month = {}
    change_month = {"01":"January",
                    "02":"February",
                    "03":"March",
                    "04":"April",
                    "05":"May",
                    "06":"June",
                    "07":"July",
                    "08":"August",
                    "09":"September",
                    "10":"October",
                    "11":"November",
                    "12":"December"}
    for x in range(0, len(data)):
        injuries = 0
        month = data[x]['Event Date'][0:2]
        try: 
            month = change_month[month]
        except KeyError:
            month = data[x]['Event Id'][4:6]
            month = change_month[month]
        if data[x]['Event Date'] != '':
            year = data[x]['Event Date'][-4:]
        else:
            year = data[x]['Event Id'][0:4]
        month = month + ' ' + year
        fatal = data[x]['Total Fatal Injuries']
        serious = data[x]['Total Serious Injuries']
        # Skip the blanks        
        if fatal:
            injuries += int(fatal)
        if serious:
            injuries += int(serious)
        injuries_by_month[month] = injuries
        injuries_by_month = Counter(injuries_by_month)        
        
    return injuries_by_month, injuries_by_month.most_common(3)
           
month_count_injuries, worst_3_months_inj  = worst_month_injuries(aviation_dict_list)

worst_3_months_inj
