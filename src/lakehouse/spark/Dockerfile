FROM apache/spark:4.0.1-python3

USER root

RUN pip install \
    delta-spark==4.1.0 \
    duckdb \
    boto3 \
    psycopg2-binary \
    pyarrow \
    pandas \
    jupyter \
    ipykernel

USER spark