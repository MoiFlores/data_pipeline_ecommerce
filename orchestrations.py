from staging_job.box_jobs.box_loaders import BoxLoaders

loader = BoxLoaders()
loader.get_data_from_mongo(
    MONGO_URI="##################### AQUI VA TU MONGO_URI ###############################",
    db_name="store", collection_name="orders")

