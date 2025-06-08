#!/usr/bin/env python3
"""
Test script for Healthcare Analytics Project.
Verifies that all components work correctly.
"""

import os
import sys
import pandas as pd
import sqlite3

# Add src directory to path
sys.path.append('./src')

def test_data_generation():
    """Test synthetic data generation."""
    print("🧪 Testing data generation...")
    
    try:
        from data_generator import generate_patient_data, generate_hospital_data
        
        # Generate small test datasets
        patient_data = generate_patient_data(100)
        hospital_data = generate_hospital_data(5)
        
        # Verify data structure
        assert patient_data.shape[0] == 100, "Patient data should have 100 rows"
        assert patient_data.shape[1] >= 10, "Patient data should have at least 10 columns"
        assert hospital_data.shape[0] == 5, "Hospital data should have 5 rows"
        assert hospital_data.shape[1] >= 9, "Hospital data should have at least 9 columns"
        
        # Check for required columns
        required_patient_cols = ['patient_id', 'hospital_id', 'age', 'diagnosis', 'readmitted']
        required_hospital_cols = ['hospital_id', 'hospital_name', 'quality_score']
        
        for col in required_patient_cols:
            assert col in patient_data.columns, f"Missing column: {col}"
        
        for col in required_hospital_cols:
            assert col in hospital_data.columns, f"Missing column: {col}"
        
        print("✓ Data generation test passed")
        return True
        
    except Exception as e:
        print(f"❌ Data generation test failed: {e}")
        return False

def test_database_operations():
    """Test database operations."""
    print("🧪 Testing database operations...")
    
    try:
        from data_generator import generate_patient_data, generate_hospital_data
        from db_utils import load_data_to_db, execute_query
        
        # Generate test data
        patient_data = generate_patient_data(50)
        hospital_data = generate_hospital_data(3)
        
        # Test database loading
        test_db = 'test_database.db'
        load_data_to_db(patient_data, hospital_data, test_db)
        
        # Test query execution
        query = "SELECT COUNT(*) as count FROM patients"
        result = execute_query(query, test_db)
        
        assert result['count'].iloc[0] == 50, "Database should contain 50 patient records"
        
        # Test join query
        join_query = """
        SELECT p.patient_id, h.hospital_name 
        FROM patients p 
        JOIN hospitals h ON p.hospital_id = h.hospital_id 
        LIMIT 5
        """
        join_result = execute_query(join_query, test_db)
        assert len(join_result) == 5, "Join query should return 5 records"
        
        # Clean up test database
        if os.path.exists(test_db):
            os.remove(test_db)
        
        print("✓ Database operations test passed")
        return True
        
    except Exception as e:
        print(f"❌ Database operations test failed: {e}")
        return False

def test_visualizations():
    """Test visualization functions."""
    print("🧪 Testing visualizations...")
    
    try:
        from data_generator import generate_patient_data
        from visualization import set_plot_style, plot_readmission_by_diagnosis
        import matplotlib.pyplot as plt
        
        # Generate test data
        patient_data = generate_patient_data(100)
        
        # Test plot creation (without showing)
        plt.ioff()  # Turn off interactive mode
        fig = plot_readmission_by_diagnosis(patient_data)
        
        assert fig is not None, "Plot function should return a figure object"
        
        # Close the figure to free memory
        plt.close(fig)
        
        print("✓ Visualization test passed")
        return True
        
    except Exception as e:
        print(f"❌ Visualization test failed: {e}")
        return False

def test_project_structure():
    """Test project file structure."""
    print("🧪 Testing project structure...")
    
    required_files = [
        'README.md',
        'requirements.txt',
        'healthcare_analysis.ipynb',
        'setup_project.py',
        'src/__init__.py',
        'src/data_generator.py',
        'src/db_utils.py',
        'src/visualization.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    
    print("✓ Project structure test passed")
    return True

def main():
    """Run all tests."""
    print("🏥 Healthcare Analytics Project - Test Suite")
    print("=" * 50)
    
    tests = [
        test_project_structure,
        test_data_generation,
        test_database_operations,
        test_visualizations
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()  # Add spacing between tests
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Project is ready to use.")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
