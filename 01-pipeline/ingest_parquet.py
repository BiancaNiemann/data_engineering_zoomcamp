#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click
import os

@click.command()
@click.option('--pg-user', required=True, help='PostgreSQL username')
@click.option('--pg-pass', required=True, help='PostgreSQL password')
@click.option('--pg-host', required=True, help='PostgreSQL host')
@click.option('--pg-port', required=True, help='PostgreSQL port')
@click.option('--pg-db', required=True, help='PostgreSQL database name')
@click.option('--target-table', required=True, help='Target table name')
@click.option('--file-path', required=True, help='Path to local parquet file')
def main(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table, file_path):
    """Ingest a local Parquet file into PostgreSQL"""
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Parquet file not found at {file_path}")

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    parquet_file = pq.ParquetFile(file_path)
    n_row_groups = parquet_file.num_row_groups
    print(f"Parquet file contains {n_row_groups} row groups")

    # Create table schema using first row group
    first_chunk = parquet_file.read_row_group(0).to_pandas()
    first_chunk.head(0).to_sql(
        name=target_table,
        con=engine,
        if_exists="replace"
    )
    print(f"Table {target_table} created")

    # Insert all row groups
    for i in tqdm(range(n_row_groups), desc="Ingesting parquet"):
        df_chunk = parquet_file.read_row_group(i).to_pandas()
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append"
        )
        print(f"Inserted row group {i + 1}/{n_row_groups}: {len(df_chunk)} rows")

    print(f"Finished ingesting parquet into {target_table}")


if __name__ == '__main__':
    main()
