from pathlib import Path
import json

path = Path('eq_data/eq_data_30_day_m1.json')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:5])
print(lats[:5])

path = Path('eq_data/readable_eq_data.json')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

