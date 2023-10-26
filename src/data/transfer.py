import json
import pandas as pd

def convert_to_feature(entry):
    location = json.loads(entry["location"].replace("'", "\""))
    feature = {
        "type": "Feature",
        "properties": {
            "name": entry["name"],
            "amenity": entry["tag"],
            "province": entry["province"],
            "city": entry["city"],
            "area": entry["area"],
            "address": entry["address"],
            "location": entry["location"],
            "detail": entry["detail"],
            "detail_info": entry["detail_info"],
            "detail_url": entry["detail_url"],
            "isin_region": entry["isin_region"],
            "行业大类": entry["行业大类"],
            "行业子类": entry["行业子类"]
        },
        "geometry": {
            "type": "Point",
            "coordinates": [float(location['lng'])-0.0111, float(location['lat'])-0.00385]
        }
    }
    return feature

def is_valid_entry(entry):
    return not pd.isna(entry["tag"])

def process_csv_to_json(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df[df.apply(is_valid_entry, axis=1)]  # 过滤掉tag为NaN的条目
    data = df.to_dict(orient='records')
    features = [convert_to_feature(entry) for entry in data]

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(features, file, ensure_ascii=False, indent=4)

for i in range(6):
    input_file = f"F:\\作品集\\前期\\Cavia_Porcellus_Culture\\cavia_porcellus_culture\\src\\data\\csv\\{i}.csv"
    output_file = f"F:\\作品集\\前期\\Cavia_Porcellus_Culture\\cavia_porcellus_culture\\src\\data\\csv\\{i}.json"
    process_csv_to_json(input_file, output_file)

# 读取五个JSON文件并将它们合并到一个列表中
file_paths = ["F:\\作品集\\前期\\Cavia_Porcellus_Culture\\cavia_porcellus_culture\\src\\data\\csv\\1.json",
              "F:\\作品集\\前期\\Cavia_Porcellus_Culture\\cavia_porcellus_culture\\src\\data\\csv\\2.json",
              "F:\\作品集\\前期\\Cavia_Porcellus_Culture\\cavia_porcellus_culture\\src\\data\\csv\\3.json",
              "F:\\作品集\\前期\\Cavia_Porcellus_Culture\\cavia_porcellus_culture\\src\\data\\csv\\4.json",
              "F:\\作品集\\前期\\Cavia_Porcellus_Culture\\cavia_porcellus_culture\\src\\data\\csv\\5.json",
              "F:\\作品集\\前期\\Cavia_Porcellus_Culture\\cavia_porcellus_culture\\src\\data\\csv\\0.json",
              ]
merged_data = []

for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        merged_data.extend(data)

# 将合并后的数据写入新的JSON文件
output_file = 'merged_data.json'

with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)

print(f'Merged data saved to {output_file}')

