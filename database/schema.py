import psycopg2

class DatabaseManager:
    def __init__(self, dbname, user, password, host):
        # Constructor for DatabaseManager class
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = None
        self.cur = None
    
    def connect(self):
        # Establish a connection to the database
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )
        self.cur = self.conn.cursor()

    def disconnect(self):
        # Close the cursor and connection
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def execute_query(self, query):
        # Execute a query and commit changes
        self.cur.execute(query)
        self.conn.commit()

    def create_schema(self, schema_name):
        # Create a schema if it doesn't exist
        create_schema_query = f"CREATE SCHEMA IF NOT EXISTS {schema_name};"
        self.execute_query(create_schema_query)

    def create_table(self,schema_name):
        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.products (
                id SERIAL PRIMARY KEY NOT NULL,
                code INTEGER NOT NULL,
                name TEXT,  
                date DATE,
                price NUMERIC(10, 2),     
                discount INTEGER                
            );
        """
        self.execute_query(create_table_query)

data_manager = DatabaseManager(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="postgres"
)

schema_name = 'CRUD'

data_manager.connect()  # Connect to the database

data_manager.create_schema(schema_name)
data_manager.create_table(schema_name)

data_manager.disconnect()  # Disconnect to the database