class pokemon():
      
  def __init__(self, json,locJson):
    """initiate the class pokemon

    Args:
        json (dict): json response from api endpoint /pokemon
        locJson (dict): json response from api endpoint /encounter
    """        
    self.json = json
    self.locJson = locJson
    self.setup()

  def setup(self):
    """
    set up the required  attributes
    """        
    self.getName()
    self.getId()
    self.getStats()
    self.getType()
    self.getLocation()

  def getStats(self):
    stats = self.json['stats']

    for stat in stats:
      setattr(self,stat['stat']['name'], stat['base_stat'])


  def getName(self): 
    self.name = self.json['name']
  
  def getType(self):
    self.types = [data['type']['name'] for data in self.json['types']]

  def getId(self):
    self.id = self.json['id']

  def getLocation(self,target='kanto'):
    self.location = []

    for loc in  self.locJson:
      locName =  loc['location_area']['name']
      if target in locName:
        locInfo = {'location_name':locName, 'method':loc['version_details'][0]['encounter_details'][0]['method']['name']}
        self.location.append(locInfo)



  
  def getData(self):
    data = vars(self)
    del data['json']
    del data['locJson']
    return data
