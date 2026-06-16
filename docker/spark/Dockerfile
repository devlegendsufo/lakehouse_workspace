FROM apache/spark:4.0.1-python3

USER root

# Python packages
RUN pip install --no-cache-dir \
    delta-spark==4.1.0 \
    duckdb \
    pandas \
    pyarrow \
    boto3 \
    s3fs \
    psycopg2-binary

# Create workspace
RUN mkdir -p /workspace

WORKDIR /workspace

USER spark

CMD ["tail", "-f", "/dev/null"]