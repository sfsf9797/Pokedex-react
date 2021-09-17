import os
from pathlib import Path
import datetime
import json 

class cache():

    def __init__(self,fileName, basePath = './data'):
        """

        Args:
            fileName ([str]): [filename for cache]
            basePath (str, optional): [the base path to the file]. Defaults to './data'.
        """        
        self.dateTimeFormat = "%Y-%m-%d %H:%M:%S"
        self.basePath = basePath
        self.filePath = os.path.join(self.basePath,fileName)
        self.setup()

    def setup(self):
        '''
        create the file if it doesn't exist using the touch method
        '''
        fle = Path(self.filePath)
        fle.touch(exist_ok=True)
        f = open(fle)

    def get(self, nameOrId):
        """get the pokemon information stored in file
        using id or name

        Args:
            nameOrId (str): name or id of pokemon

        Raises:
            KeyError: if the name or id is not found

        Returns:
            [dict]: pokemon's information
        """        

        with open(self.filePath, "r") as f:
            lines = f.readlines()
        for line in lines:
            #check if the string before the first whitespace equal to the name or id
            if line[0 : line.find(' ')] == str(nameOrId): 
                data = line.strip('/n')[line.find(' ')+1:]
                data = json.loads(data.replace('\'','\"'))
                return data

        raise KeyError('name or id not found')

    def save(self, data):
        """save the data in the text file

        Args:
            data (dict): pokemon's information
        """       

        with open(self.filePath, 'a') as f:
            f.write(data)

    def remove(self,nameOrId):
        """
        remove the line  if the line contains the name or id

        Args:
            nameOrId (str): name or id of pokemon
        """       

        with open(self.filePath, "r") as f:
            lines = f.readlines()

        with open(self.filePath, "w") as f:
            for line in lines:
                if line[0 : line.find(' ')] != str(nameOrId):
                    f.write(line)

    def contain(self,nameOrId):
        """
        check if the name or id exist in the file

        Args:
            nameOrId (str): name or id of pokemon
        """       
        with open(self.filePath, "r") as f:
            lines = f.readlines()
        for line in lines:
            if line[0 : line.find(' ')] == str(nameOrId):
                return True
        return False

class name2Id(cache):
    '''
    match the pokemon's name to its id
    '''

    def __init__(self):
        super().__init__('name2Id.txt')

    def get(self, id):
        try:
            return super().get(id)
        except:
            return None
        
    def save(self,data):
        if not self.contain(data['name']):
            data = str(data['name']) + " " + str(data['id']) + " " + "\n"
            super().save(data)

    

class Id2Json(cache):
    '''
    match id to the json data
    '''

    def __init__(self):
        super().__init__('Id2Json.txt')

    
    def save(self, data):
             
        currentTime = datetime.datetime.now().strftime(self.dateTimeFormat)
        data['timeStamp'] = currentTime
        
        data = str(data['id']) + " " +  str(data) + " " + '\n'

        super().save(data)

    def get(self,id):
        """
        return data that is not expired else return none

        Args:
            id (str) pokemon's id

        Returns:
            data: pokemon's information
        """        

        try:
            data = super().get(id)
        except:
            return None

        
        if self.checkExpiry(data['timeStamp']):
            self.remove(id)
            data = None

        return data

    def checkExpiry(self,timeStamp):
        start = datetime.datetime.strptime(timeStamp, self.dateTimeFormat)
        delta = datetime.datetime.now() - start

        return delta.days >= 7
        


