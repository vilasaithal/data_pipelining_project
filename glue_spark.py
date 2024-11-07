import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Albums
Albums_node1730773368272 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://e2e-dataengg-project/staging/albums.csv"], "recurse": True}, transformation_ctx="Albums_node1730773368272")

# Script generated for node Tracks
Tracks_node1730773368842 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://e2e-dataengg-project/staging/tracks.csv"], "recurse": True}, transformation_ctx="Tracks_node1730773368842")

# Script generated for node Artists
Artists_node1730773368565 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://e2e-dataengg-project/staging/artists.csv"], "recurse": True}, transformation_ctx="Artists_node1730773368565")

# Script generated for node Artists & Albums
ArtistsAlbums_node1730773445240 = Join.apply(frame1=Artists_node1730773368565, frame2=Albums_node1730773368272, keys1=["id"], keys2=["artist_id"], transformation_ctx="ArtistsAlbums_node1730773445240")

# Script generated for node & Tracks
Tracks_node1730774148681 = Join.apply(frame1=Tracks_node1730773368842, frame2=ArtistsAlbums_node1730773445240, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Tracks_node1730774148681")

# Script generated for node Drop Fields
DropFields_node1730774217355 = DropFields.apply(frame=Tracks_node1730774148681, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1730774217355")

# Script generated for node Target
Target_node1730774309024 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1730774217355, connection_type="s3", format="glueparquet", connection_options={"path": "s3://e2e-dataengg-project/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Target_node1730774309024")

job.commit()