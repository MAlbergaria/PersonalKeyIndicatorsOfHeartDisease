import pyodbc


class Database():

    def __init__(self, cnxn, args) -> None:
        self.cursor = pyodbc.connect(self.__get_cnxn(cnxn, args)).cursor()
        

    def __get_cnxn(self, cnxn, args):  
        cnxn_split = cnxn.split("?")
        connection = []

        for i in range(min(len(args), len(cnxn) + 1)):
            connection.append(cnxn_split[i])
            connection.append(args[i])

        connection.append(cnxn_split[-1])
            
        return "".join(connection)

