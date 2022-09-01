# BANK_API
### Database Setup
 - Database Type : PostgreSQL 14
 - DB_NAME=[db]
 - Tables, Sequences & Indexes
 ```
 CREATE SEQUENCE IF NOT EXISTS tbl_oid_seq START with 10000;

CREATE SEQUENCE IF NOT EXISTS tbl_aid_seq START with 100;


CREATE TABLE IF NOT EXISTS online_account 
(
  oid integer NOT NULL DEFAULT NEXTVAL('tbl_oid_seq'::regclass), 
  created_at timestamptz NOT NULL DEFAULT now(), 
  verified_account boolean NOT NULL DEFAULT false,
  email VARCHAR (50) UNIQUE,
  passwd VARCHAR (200),
  first_name VARCHAR (50),
  last_name VARCHAR (50),
  address VARCHAR (100),
  CONSTRAINT pkey_tbl PRIMARY KEY ( oid )
);

CREATE TABLE IF NOT EXISTS admin_account 
(
  aid integer NOT NULL DEFAULT NEXTVAL('tbl_aid_seq'::regclass), 
  created_at timestamptz NOT NULL DEFAULT now(), 
  email VARCHAR (50) UNIQUE,
  passwd VARCHAR (200),
  first_name VARCHAR (50),
  last_name VARCHAR (50),
  department VARCHAR (100),
  CONSTRAINT pkey_tbl_aid PRIMARY KEY ( aid )
);

CREATE INDEX IF NOT EXISTS search_email ON online_account( email );

CREATE INDEX IF NOT EXISTS search_pii ON online_account( first_name, last_name, email );

 ```

### Application Environment Setup

#### Python Version
```
python --version               
Python 3.10.1
```

#### Activate Virtual Environment
```
source venv/bin/activate
```

#### Install PIP
```
python -m pip install --upgrade pip
```

#### Install Application Dependencies
```
pip install -r requirements.txt
```

#### Export Application Environment
```
export SECRET_KEY=[JWT_SECRET_KEY]
export ALGORITHM=HS256
export ACCESS_TOKEN_EXPIRE_MINUTES=3600
export DB_NAME=[db]
export DB_HOST=[db_host]
export DB_USER=[db_user]
export DB_PASS=[db_pass]
```

#### Start the API
```
uvicorn app.main:app --reload
```
