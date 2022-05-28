import requests
import pandas as pd
from sqlalchemy import create_engine

areas = ["africa", "america", "asia", "australia", "europe"]
engine = create_engine('sqlite:///data/xeno_canto.sqlite', echo=False)
for area in areas:
	result = requests.get(f"https://www.xeno-canto.org/api/2/recordings?query=area:{area}")
	num_pages = result.json()["numPages"]
	for page in range(1, num_pages):
		result = requests.get(f"https://www.xeno-canto.org/api/2/recordings?query=area:{area}&page={page}")
		recordings = result.json()["recordings"]
		if len(recordings) == 0:
			continue
		df = pd.json_normalize(recordings, meta=[
			["sono", "small"],
			["sono", "med"],
			["sono", "large"],
			["sono", "full"]
		])
		df["area"] = area
		df["page"] = page
		df['also'] = df['also'].apply(lambda x: ','.join(x).strip())

		print(f"{area} page {page} of {num_pages}")
		with engine.begin() as connection:
			df.to_sql('recordings', con=connection, if_exists='append')
