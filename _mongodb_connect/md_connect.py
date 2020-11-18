# %%
from pymongo import MongoClient as MC
class Database(object):
    DATABASE = None
    DATABASE_NAME = None
    USERNAME = 'krzyzaku'
    PASSWORD = 'krzyzaku'
    URI = f'mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.hagff.mongodb.net'
    CLIENT = None
    COLLECTION_NAME = None
    COLLECTION = None

# TODO - login_db - połączenie klienta z mongodb
    @classmethod
    def login_db(cls):
        client = MC(cls.URI)
        cls.CLIENT = client
        return cls.CLIENT
# TODO - check_db - wybór bazy danych mongodb
    @classmethod
    def check_db(cls):
        db_list = cls.CLIENT.list_database_names()
        print("Exists databases {}".format(db_list))
        DATABASE_NAME = input(str("podaj baze"))
        if (DATABASE_NAME in db_list) is True:
            print("Connect to database {}".format(DATABASE_NAME))
            cls.DATABASE = cls.CLIENT[DATABASE_NAME]
        else:
            print(f"Wrong database name {DATABASE_NAME}")
        return cls.DATABASE
# TODO - start_collections - wybór startowej kolekcji
    @classmethod
    def start_collections(cls, name):
        collection_list = cls.DATABASE.list_collection_names()
        print(collection_list)
        cls.COLLECTION_NAME = name
        cls.COLLECTION = cls.DATABASE[cls.COLLECTION_NAME]
        return cls.COLLECTION
# TODO - check_collection - sprawdzanie kolekcji i dodawanie jej
    @classmethod
    def check_collection(cls):
        collection_list = cls.DATABASE.list_collection_names()
        print("Exists collections: ", collection_list)
        cls.COLLECTION_NAME = str(input("Add collection name: "))
        if (cls.COLLECTION_NAME in collection_list) is True:
            print(f"This collection {cls.COLLECTION_NAME} exists in {collection_list}")
            cls.COLLECTION = cls.DATABASE[cls.COLLECTION_NAME]
        else:
            print(f"This: {cls.COLLECTION_NAME} don't exist in datebase {collection_list}")
            as_chose = str(input(r"Write 'y' if you want create collection or write 'n' if you don't"))
            if as_chose == "y":
                cls.DATABASE.create_collection(cls.COLLECTION_NAME)
                print(f"Created new collection: {cls.COLLECTION_NAME} in datebase {cls.CLIENT.list_database_names()}")
                collection_list = cls.DATABASE.list_collection_names()
                print(collection_list)
                cls.COLLECTION = cls.DATABASE[cls.COLLECTION_NAME]
            else:
                print(collection_list)
                raise Exception("Collection don't create or wrong word'")
# TODO - del_collection - usuwanie podanej kolekcji
    @staticmethod
    def del_collection(fn):
        fn.drop()
# TODO - del_database - usuwanie podanej bazy danych
    @classmethod
    def del_database(cls, name):
        client = MC(cls.URI)
        db_list = client.database_names()
        print("List of databases", db_list)
        as_chose = str(input(r"Write 'y' if you want delete database 'n' if you don't"))
        if as_chose == "y":
            client.drop_database(name)
            print("Done")
        else:
            raise Exception("Cancel action")
# TODO - insert_one - dodawanie dokumentów do kolekcji
    @staticmethod
    def insert_one(fn, dict_name):
        return fn.insert_one(dict_name)
# TODO - create_dict - tworenie dokumentacji
    @staticmethod
    def create_dict(dict_name, pairs):
        i = 0
        id_value = int(input("podaj nr id"))
        dict_name["_id"] = id_value
        while i != pairs:
            key = input("podaj wartość klucza")
            value = input("podaj wartość do klucza")
            dict_name[key] = value
            i += 1
        else:
            return dict_name

    @staticmethod
    def check_dict_id(fn, numer_id):
        # ! for x in fn.find({"_id": numer_id},{}):
        for x in fn.find({"_id": numer_id},{}):
            return x


Database.login_db()
Database.check_db()
test_dict = {}
# Database.create_dict(test_dict, 4)
a = Database.start_collections("ttt")
# Database.insert_one(a, test_dict)
b = Database.check_dict_id(a, 0)
print(b)
# Database.del_collection(a)
# Database.check_collection()
# Database.del_database("test2")
# Database.del_collection("ttt")

# %%
