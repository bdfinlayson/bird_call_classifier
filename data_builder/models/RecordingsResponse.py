import json

class Sono:
	def __init__(self, json_obj):
		self.__dict__ = json.loads(json_obj)

	small: str
	med: str
	large: str
	full: str

class Recordings:
	def __init__(self, json_obj):
		j = json.loads(json_obj)
		self.__dict__ = j
		self.file_name = j['file-name']

	id: str
	gen: str
	sp: str
	ssp: str
	en: str
	rec: str
	cnt: str
	loc: str
	lat: str
	lng: str
	alt: str
	type: str
	url: str
	file: str
	file_name: str



class RecordingsResponse:
	def __init__(self, json_obj):
		self.__dict__ = json.loads(json_obj)

	numRecordings: str
	numSpecies: str
	page: int
	numPages: int
	recordings: [Recordings]

