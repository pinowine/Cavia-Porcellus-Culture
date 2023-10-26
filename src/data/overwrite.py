import json

f= []
d= 0.0057
t= 0.0050
lat0= 30.2571
lng0= 120.1049
center = []
bounds = []
src = []

def convert_to_feature(entry):
    for i in range(entry):
        center0 = []
        bounds0= []
        for x in range(6):
            for y in range(6):
                center0.append([lat0+t*y*2+t,lng0+d*x*2+d])
                bounds0.append([[lat0+t*y*2,lng0+d*x*2],[lat0+t*(y+1)*2,lng0+d*(x+1)*2]])
                src.append(str(x)+'_'+str(y))
            center.append(center0)
            bounds.append(bounds0)
        feature = {
            'id' : i+1,
            'title' : 'Unsolved',
            'sim_title' : '?',
            'solved' : False,
            'dpt' : 'This area will be discovered in the coming series.',
            'src' : src[i],
            'center' : center0[i],
            'bounds' : bounds0[i],
        }
        f.append(feature)
    return f

def process_json(output_file):

    features = convert_to_feature(36)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(features, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    output_file = "F:\作品集\前期\Cavia_Porcellus_Culture\cavia_porcellus_culture\src\data\mesh.json"  # 输出JSON文件名
    process_json(output_file)
