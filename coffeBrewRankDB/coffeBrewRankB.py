import sqlite3 

createRankingTable = "CREATE TABLE IF NOT EXISTS ranking (id INTEGER PRIMARY KEY, name TEXT UNIQUE, method TEXT, rating INTEGER);"

insertRanking = "INSERT OR IGNORE INTO ranking (name, method, rating) VALUES (?, ?, ?);"

getAllRanking = "SELECT * FROM ranking ORDER BY rating DESC;"

getRankingBYName  = "SELECT * FROM ranking WHERE name = ?;"

getBestRankingBYName ="""
    SELECT * FROM ranking
    WHERE name = ?
    ORDER BY rating DESC
    LIMIT 1;""" 

class Database:
    def __init__(self) -> None:
        self.con = sqlite3.connect("coffe.db")
        self.cur = self.con.cursor()
        self.createTables()
        
    def createTables(self):
        self.cur.execute(createRankingTable)
    
    def addRow(self,name,method,rating):
            self.cur.execute(insertRanking, (name, method, rating))
            self.con.commit()
    
    def getAll(self):
            return self.cur.execute(getAllRanking).fetchall()
    
    def getbyname(self,name):
        return self.cur.execute(getRankingBYName, (name,)).fetchall()
    
    def getBestPrep(self,name):
        return self.cur.execute(getBestRankingBYName, (name,)).fetchone()
    
    









