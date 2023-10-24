import json
import os

def read_json_files_in_folder(folder_path):
    occupations_over_60 = []
    total_volume = 0
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            print(f"Reading file: {filename}")
            with open(os.path.join(folder_path, filename), 'r') as f:
                data = json.load(f)
                print(f"Data in file: {data}")
                
                if len(data) < 2:
                    continue
                category_name = data[0]
                occupation_categories = data[1]
                
                for occupation_category in occupation_categories:
                    if len(occupation_category) < 2:
                        continue
                    occupation_category_name = occupation_category[0]
                    individual_occupations = occupation_category[1]
                    
                    for occupation in individual_occupations:
                        if len(occupation) < 8:
                            continue
                        occupation_name = occupation[0]
                        occupation_link = occupation[1]
                        occupation_percent = occupation[2]
                        occupation_volume = occupation[-1]
                       
                        try:
                            occupation_volume_value = int(occupation_volume.replace(',', ''))
                        except ValueError:
                            continue
                        
                        try:
                            occupation_percent_value = float(occupation_percent.strip('%'))
                        except ValueError:
                            continue
                        
                        if occupation_percent_value > 60:                                                                                #change the number for #% OR HIGHER. (ex. if you want jobs at 70% risk or higher type 70.)
                            print(f"Adding occupation: {occupation_name}")
                            occupations_over_60.append((occupation_name, occupation_percent_value, occupation_volume_value))
                            total_volume += occupation_volume_value  
    
    occupations_over_60.sort(key=lambda x: x[1])
    
    return occupations_over_60, total_volume

def write_to_text_file(sorted_occupations, total_volume):
    with open("occupations_output.txt", "w") as f:
        f.write("Occupations over 60% sorted from lowest to highest:\n")
        f.write("==================================================\n\n")
        for occupation_name, occupation_percent, occupation_volume in sorted_occupations:
            formatted_volume = format(occupation_volume, ',')
            f.write(f"{occupation_name}: {occupation_percent}% - Volume: {formatted_volume}\n\n")
        f.write("==================================================\n")
        formatted_total_volume = format(total_volume, ',')
        f.write(f"Total Jobless: {formatted_total_volume}\n")

if __name__ == '__main__':
    folder_path = os.path.dirname(os.path.abspath(__file__))
    print(f"Folder path: {folder_path}")  
    sorted_occupations, total_volume = read_json_files_in_folder(folder_path)
    
    print("Occupations over 60% sorted from lowest to highest:")
    for occupation_name, occupation_percent, occupation_volume in sorted_occupations:
        print(f"{occupation_name}: {occupation_percent}% - Volume: {occupation_volume}")
        
    print(f"Total Jobless: {total_volume}")  
    
    write_to_text_file(sorted_occupations, total_volume) 
