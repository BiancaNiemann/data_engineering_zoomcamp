import pandas as pd
from sqlalchemy import create_engine
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pg-user', required=True)
    parser.add_argument('--pg-pass', required=True)
    parser.add_argument('--pg-host', required=True)
    parser.add_argument('--pg-port', required=True)
    parser.add_argument('--pg-db', required=True)
    parser.add_argument('--target-table', required=True)
    parser.add_argument('--csv-file', required=True)
    parser.add_argument('--chunksize', type=int, default=1000)

    args = parser.parse_args()

    engine = create_engine(
        f'postgresql://{args.pg_user}:{args.pg_pass}@{args.pg_host}:{args.pg_port}/{args.pg_db}'
    )

    df_iter = pd.read_csv(args.csv_file, iterator=True, chunksize=args.chunksize)

    for i, df in enumerate(df_iter):
        df.to_sql(
            name=args.target_table,
            con=engine,
            if_exists='append' if i > 0 else 'replace',
            index=False
        )
        print(f'Inserted chunk {i + 1}')

if __name__ == "__main__":
    main()
