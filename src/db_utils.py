"""
Database utilities for the Healthcare Analytics project.
Handles database creation, data loading, and SQL queries.
"""

import sqlite3
import pandas as pd
import os

def create_database(db_path='database.db'):
    """
    Create SQLite database and tables for the project.
    
    Parameters:
    -----------
    db_path : str
        Path to the SQLite database file
    
    Returns:
    --------
    sqlite3.Connection
        Connection to the SQLite database
    """
    conn = sqlite3.connect(db_path)
    
    # Create patients table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id TEXT PRIMARY KEY,
        hospital_id TEXT,
        age INTEGER,
        gender TEXT,
        diagnosis TEXT,
        treatment TEXT,
        admission_date TEXT,
        discharge_date TEXT,
        length_of_stay INTEGER,
        readmitted BOOLEAN,
        days_to_readmission INTEGER,
        insurance_type TEXT,
        FOREIGN KEY (hospital_id) REFERENCES hospitals(hospital_id)
    )
    ''')
    
    # Create hospitals table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS hospitals (
        hospital_id TEXT PRIMARY KEY,
        hospital_name TEXT,
        region TEXT,
        hospital_type TEXT,
        bed_count INTEGER,
        staff_count INTEGER,
        is_teaching_hospital BOOLEAN,
        quality_score REAL,
        specialties TEXT
    )
    ''')
    
    return conn

def load_data_to_db(patient_data, hospital_data, db_path='database.db'):
    """
    Load data from DataFrames into SQLite database.
    
    Parameters:
    -----------
    patient_data : pandas.DataFrame
        DataFrame containing patient data
    hospital_data : pandas.DataFrame
        DataFrame containing hospital data
    db_path : str
        Path to the SQLite database file
    """
    conn = create_database(db_path)
    
    # Convert boolean columns to integers for SQLite compatibility
    patient_data_copy = patient_data.copy()
    patient_data_copy['readmitted'] = patient_data_copy['readmitted'].astype(int)
    
    hospital_data_copy = hospital_data.copy()
    hospital_data_copy['is_teaching_hospital'] = hospital_data_copy['is_teaching_hospital'].astype(int)
    
    # Load data into tables
    patient_data_copy.to_sql('patients', conn, if_exists='replace', index=False)
    hospital_data_copy.to_sql('hospitals', conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()
    
    print(f"Data loaded into database: {db_path}")

def execute_query(query, db_path='database.db', params=None):
    """
    Execute SQL query and return results as DataFrame.
    
    Parameters:
    -----------
    query : str
        SQL query to execute
    db_path : str
        Path to the SQLite database file
    params : tuple, optional
        Parameters for the SQL query
        
    Returns:
    --------
    pandas.DataFrame
        Query results as DataFrame
    """
    conn = sqlite3.connect(db_path)
    
    if params:
        result = pd.read_sql_query(query, conn, params=params)
    else:
        result = pd.read_sql_query(query, conn)
    
    conn.close()
    return result