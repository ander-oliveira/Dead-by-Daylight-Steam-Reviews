from glob import glob
import json
import datetime as dt


def process_all_data(path, all_data = []):
    for file in glob(path):
        with open(file, encoding='latin-1') as json_file:    
            data = json.load(json_file)
            for review in data['reviews']:
                aux = {}
                for k,v in review.items():
                    if k == 'author':
                        for a, b in v.items():
                            if a == 'last_played':
                                aux[a] = dt.datetime.utcfromtimestamp(b).strftime("%Y/%m/%d")
                            else:
                                aux[a] = b
                    elif k == 'timestamp_created' or k == 'timestamp_updated':
                        aux[k] = dt.datetime.utcfromtimestamp(v).strftime("%Y/%m/%d")
                    else:
                        aux[k] = v
                all_data.append(aux)
    return all_data


def write_to_json(data, file_output):
    with open(file_output, "w", encoding='latin-1') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    

if __name__ == "__main__":
    path_to_data = 'data/*.json'
    outfile = 'all_dbd_reviews.json'
    data = process_all_data(path_to_data)
    write_to_json(data, outfile)