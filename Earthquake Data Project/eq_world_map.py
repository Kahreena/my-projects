import plotly.express as px

from eq_explore_data import all_eq_dicts, lats, lons, mags

for eq_dict in all_eq_dicts:

    title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     )

fig.show()
