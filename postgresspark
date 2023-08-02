import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


connection_postgres_options = {
    "url": "jdbc:postgresql://database-8.cluster-fdsfds.us-east-1.rds.amazonaws.com:5432/postgres",
    "dbtable": "public.table1",
    "user": "postgres",
    "password": "***",
    "customJdbcDriverS3Path": "s3://bucket/lib/postgresql-42.2.19.jar",
    "customJdbcDriverClassName": "org.postgresql.Driver"}
    

dyf = glueContext.create_dynamic_frame.from_options(connection_type="postgresql",connection_options=connection_postgres_options)
dyf.printSchema()
dyf.show()


job.commit()
