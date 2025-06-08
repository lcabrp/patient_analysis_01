"""
Data Generator for Healthcare Analytics Project.
Creates synthetic patient and hospital datasets for analysis.
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random

def generate_patient_data(num_records=3500):
    """
    Generate synthetic patient data.
    
    Parameters:
    -----------
    num_records : int
        Number of patient records to generate
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame containing synthetic patient data
    """
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Patient demographics
    patient_ids = [f"P{i:06d}" for i in range(1, num_records + 1)]
    ages = np.random.normal(65, 15, num_records).astype(int)
    ages = np.clip(ages, 18, 95)  # Limit age range
    
    genders = np.random.choice(['M', 'F'], size=num_records)
    
    # Hospital assignment (will match with hospital dataset)
    hospital_ids = np.random.choice([f"H{i:03d}" for i in range(1, 21)], size=num_records)
    
    # Clinical data
    diagnoses = np.random.choice([
        'Diabetes', 'Heart Failure', 'Pneumonia', 'COPD', 
        'Stroke', 'Kidney Disease', 'Cancer', 'Hypertension'
    ], size=num_records)
    
    # Treatment data
    treatments = []
    for diagnosis in diagnoses:
        if diagnosis == 'Diabetes':
            treatments.append(np.random.choice(['Insulin', 'Metformin', 'Lifestyle Changes']))
        elif diagnosis == 'Heart Failure':
            treatments.append(np.random.choice(['ACE Inhibitors', 'Beta Blockers', 'Diuretics']))
        elif diagnosis == 'Pneumonia':
            treatments.append(np.random.choice(['Antibiotics', 'Respiratory Therapy', 'Oxygen']))
        elif diagnosis == 'COPD':
            treatments.append(np.random.choice(['Bronchodilators', 'Steroids', 'Oxygen Therapy']))
        elif diagnosis == 'Stroke':
            treatments.append(np.random.choice(['Thrombolytics', 'Anticoagulants', 'Rehabilitation']))
        elif diagnosis == 'Kidney Disease':
            treatments.append(np.random.choice(['Dialysis', 'Medication', 'Dietary Changes']))
        elif diagnosis == 'Cancer':
            treatments.append(np.random.choice(['Chemotherapy', 'Radiation', 'Surgery']))
        else:  # Hypertension
            treatments.append(np.random.choice(['ACE Inhibitors', 'Diuretics', 'Beta Blockers']))
    
    # Length of stay
    length_of_stay = np.random.lognormal(1.5, 0.5, num_records).astype(int)
    length_of_stay = np.clip(length_of_stay, 1, 30)  # Limit stay between 1 and 30 days
    
    # Admission and discharge dates
    end_date = datetime.now()
    admission_dates = []
    discharge_dates = []

    for stay in length_of_stay:
        # Convert numpy int64 to regular Python int
        days_back = int(np.random.randint(1, 365))
        stay_days = int(stay)

        discharge = end_date - timedelta(days=days_back)
        admission = discharge - timedelta(days=stay_days)
        admission_dates.append(admission)
        discharge_dates.append(discharge)
    
    # Readmission data
    readmitted = np.random.choice([True, False], size=num_records, p=[0.18, 0.82])  # 18% readmission rate
    
    readmission_days = []
    for readmit in readmitted:
        if readmit:
            readmission_days.append(int(np.random.randint(1, 31)))  # Readmitted within 30 days
        else:
            readmission_days.append(None)
    
    # Insurance type
    insurance = np.random.choice(['Medicare', 'Medicaid', 'Private', 'Uninsured'], 
                                size=num_records, 
                                p=[0.45, 0.25, 0.25, 0.05])
    
    # Create DataFrame
    patient_data = pd.DataFrame({
        'patient_id': patient_ids,
        'hospital_id': hospital_ids,
        'age': ages,
        'gender': genders,
        'diagnosis': diagnoses,
        'treatment': treatments,
        'admission_date': admission_dates,
        'discharge_date': discharge_dates,
        'length_of_stay': length_of_stay,
        'readmitted': readmitted,
        'days_to_readmission': readmission_days,
        'insurance_type': insurance
    })
    
    return patient_data

def generate_hospital_data(num_hospitals=20):
    """
    Generate synthetic hospital data.
    
    Parameters:
    -----------
    num_hospitals : int
        Number of hospitals to generate
        
    Returns:
    --------
    pandas.DataFrame
        DataFrame containing synthetic hospital data
    """
    np.random.seed(42)
    
    hospital_ids = [f"H{i:03d}" for i in range(1, num_hospitals + 1)]
    
    hospital_names = [
        "Memorial Hospital", "University Medical Center", "Community Hospital",
        "Regional Medical Center", "General Hospital", "St. Mary's Hospital",
        "Mercy Medical Center", "County Hospital", "Metropolitan Hospital",
        "Sacred Heart Hospital", "Providence Hospital", "Hope Medical Center",
        "Valley Hospital", "Riverside Medical Center", "Central Hospital",
        "Highland Hospital", "Lakeside Medical Center", "Summit Hospital",
        "Oakwood Hospital", "Pinecrest Medical Center"
    ]
    
    regions = np.random.choice(['Northeast', 'Southeast', 'Midwest', 'Southwest', 'West'], size=num_hospitals)
    
    hospital_types = np.random.choice(['Urban', 'Suburban', 'Rural'], 
                                     size=num_hospitals, 
                                     p=[0.5, 0.3, 0.2])
    
    bed_counts = []
    for hospital_type in hospital_types:
        if hospital_type == 'Urban':
            bed_counts.append(int(np.random.randint(300, 800)))
        elif hospital_type == 'Suburban':
            bed_counts.append(int(np.random.randint(150, 400)))
        else:  # Rural
            bed_counts.append(int(np.random.randint(50, 200)))

    staff_counts = [int(beds * np.random.uniform(3.5, 5.5)) for beds in bed_counts]
    
    teaching_hospitals = np.random.choice([True, False], size=num_hospitals, p=[0.3, 0.7])
    
    quality_scores = np.random.normal(3.5, 0.8, num_hospitals)
    quality_scores = np.clip(quality_scores, 1, 5).round(1)  # 1-5 scale, rounded to 1 decimal
    
    specialties = []
    for _ in range(num_hospitals):
        num_specialties = np.random.randint(2, 6)
        specialty_list = np.random.choice([
            'Cardiology', 'Oncology', 'Neurology', 'Orthopedics', 
            'Pediatrics', 'Geriatrics', 'Pulmonology', 'Gastroenterology'
        ], size=num_specialties, replace=False)
        specialties.append(', '.join(specialty_list))
    
    # Create DataFrame
    hospital_data = pd.DataFrame({
        'hospital_id': hospital_ids,
        'hospital_name': hospital_names,
        'region': regions,
        'hospital_type': hospital_types,
        'bed_count': bed_counts,
        'staff_count': staff_counts,
        'is_teaching_hospital': teaching_hospitals,
        'quality_score': quality_scores,
        'specialties': specialties
    })
    
    return hospital_data

def save_datasets():
    """Generate and save both datasets to the data directory."""
    # Create data directory if it doesn't exist
    os.makedirs('./data', exist_ok=True)

    # Generate datasets
    patient_data = generate_patient_data(3500)
    hospital_data = generate_hospital_data(20)

    # Save to CSV
    patient_data.to_csv('./data/patient_data.csv', index=False)
    hospital_data.to_csv('./data/hospital_data.csv', index=False)

    print(f"Generated patient dataset with {len(patient_data)} records")
    print(f"Generated hospital dataset with {len(hospital_data)} records")

    return patient_data, hospital_data

if __name__ == "__main__":
    save_datasets()