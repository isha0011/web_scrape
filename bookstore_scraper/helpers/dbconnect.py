# importing the module

from sqlalchemy import create_engine
# from db_utils import decode


def conn_db(cred):
    try:
        engine = create_engine(
            f"mysql+mysqldb://{cred['user']}:{cred['password']}@{cred['host']}/{cred['database']}")
        return engine
    except Exception as err:
        print(err)

# def conn_db_postgres(cred):
#     try:
#         engine = create_engine(
#             f"mysql+mysqldb://{cred['user']}:{cred['password']}@{cred['host']}/{cred['database']}")
#         return engine
#     except Exception as err:
#         print(err)
