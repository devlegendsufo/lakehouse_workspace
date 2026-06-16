from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

import os


def get_spark(app_name="lakehouse"):

    os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"

    builder = (

        SparkSession.builder

        .master("local[*]")

        .appName(app_name)

        # Delta
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension",
        )

        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )

        # MinIO
        .config(
            "spark.hadoop.fs.s3a.endpoint",
            "http://localhost:9000",
        )

        .config(
            "spark.hadoop.fs.s3a.access.key",
            "minio_admin",
        )

        .config(
            "spark.hadoop.fs.s3a.secret.key",
            "minio_enterprise_password",
        )

        .config(
            "spark.hadoop.fs.s3a.path.style.access",
            "true",
        )

        .config(
            "spark.hadoop.fs.s3a.connection.ssl.enabled",
            "false",
        )

        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem",
        )

        # Spark defaults
        .config(
            "spark.sql.shuffle.partitions",
            "8",
        )

        .config(
            "spark.sql.adaptive.enabled",
            "true",
        )

        .config(
            "spark.driver.memory",
            "2g",
        )

        .config(
            "spark.executor.memory",
            "2g",
        )

        .config(
            "spark.ui.port",
            "4050",
        )
    )

    return configure_spark_with_delta_pip(
        builder,
        extra_packages=[
            "org.apache.hadoop:hadoop-aws:3.4.1",
        ],
    ).getOrCreate()