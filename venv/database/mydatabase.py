from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

#Global Variables
SQLITE                   = 'sqlite'

#Table Names
USERS           = 'users'
ADDRESSES         = 'addresses'

class MyDatabase:

    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
    }

    #Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='',dbname=''):
        dbtype = dbtype.lower()
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)

            self.db_engine = create_engine(engine_url)
            print(self.db_engine)

        else:
            print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        metadata = MetaData()
        users = Table(USERS, metadata,
                        Column('id', Integer, primary_key=True),
                        Column('first_name', String),
                        Column('last_name',String)
                        )
        address = Table(ADDRESSES, metadata,
                        Column('id', Integer, primary_key=True),
                        Column('user_id', None, ForeignKey('users.id')),
                        Column('email', String, nullable=False),
                        Column('address', String)
                        )

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occured during Table creation!")
            print(e)

    #INsert, Update, Delete
    def excute_query(self, query=''):
        if query == '':return
        print(query)

        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)


    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)

        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row) #print(row[0],row[1],row[3])
                result.close()

        print("\n")
'''
        query = "SELECT first_name, last_name FROM {TBL_USER} WHERE " \
                "last_name LIKE 'M%';".format(TBL_USER=USERS)
        self.print_all_data(query=query)

        query = "SELECT u.last_name as last_name, " \
                "a.email as email, a.address as address " \
                "FROM {TBLUSR} AS u " \
                "LEFT JOIN {TBL_ADDR} as a " \
                "WHERE u.id=a.user_id AND u.last_name LIKE 'M%';" \
            .format(TBLUSR=USERS, TBL_ADDR=ADDRESSES)
        self.print_all_data(query=query)

    def sample_delete(self):
        query = "DELETE FROM {} WHERE id=3".format(USERS)
        self.excute_query(query)
        self.print_all_data(USERS)

    def sample_insert(self):
        query = "INSERT INTO {}(id,first_name,last_name)" \
            "VALUES (3,'John', 'Mario');".format(USERS)
        self.excute_query(query)
        self.print_all_data(USERS)

    def sample_update(self):
        query = "UPDATE {} set first_name='XXX' WHERE id={id}"\
            .format(USERS,id=3)
        self.excute_query(query)
        self.print_all_data(USERS)

'''






