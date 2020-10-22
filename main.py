from database import mydatabase

def main():
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname="mydb.sqlite")

    dbms.create_db_tables()

    dbms.print_all_data(mydatabase.USERS)
    dbms.print_all_data(mydatabase.ADDRESSES)

    #dbms.sample_query()
    #dbms.sample_delete()
    #dbms.sample_insert()
    #dbms.sample_update()



if __name__ == "__main__":main()

