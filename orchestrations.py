from staging_job.box_jobs.box_loaders import BoxLoaders
from staging_job.mysql_jobs.mysql_loaders import MySQLoaders

loader_box = BoxLoaders()
loader_mysql = MySQLoaders()

loader_box.get_data_from_mongo(
    MONGO_URI="",
    db_name="store", collection_name="orders")

loader_mysql.insert_from_json()