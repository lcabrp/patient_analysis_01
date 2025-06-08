#!/usr/bin/env python3
"""
Setup script for Healthcare Analytics Project.
Run this script to generate datasets and initialize the database.
"""

import os
import sys

# Add src directory to path
sys.path.append('./src')

from data_generator import save_datasets

def main():
    """Initialize the healthcare analytics project."""
    print("🏥 Healthcare Analytics Project Setup")
    print("=" * 50)
    
    # Create necessary directories
    print("📁 Creating project directories...")
    os.makedirs('./data', exist_ok=True)
    print("✓ Created ./data directory")
    
    # Generate datasets
    print("\n📊 Generating synthetic datasets...")
    try:
        patient_data, hospital_data = save_datasets()
        print(f"✓ Generated patient dataset: {len(patient_data):,} records")
        print(f"✓ Generated hospital dataset: {len(hospital_data):,} records")
    except Exception as e:
        print(f"❌ Error generating datasets: {e}")
        return False
    
    # Note: Database will be created in the analysis notebook after feature engineering
    
    print("\n🎉 Dataset generation completed successfully!")
    print("\nNext steps:")
    print("1. Open healthcare_analysis.ipynb in Jupyter Notebook")
    print("2. Run all cells to see the complete analysis")
    print("3. The notebook will create the database after feature engineering")
    print("4. Explore the generated visualizations and insights")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
