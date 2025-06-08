#!/usr/bin/env python3
"""
Verification script to confirm all updates for 3,500 patient records.
This script checks that all files have been properly updated.
"""

import os
import re

def check_data_generator():
    """Check that data_generator.py uses 3500 records."""
    print("🔍 Checking data_generator.py...")
    
    with open('src/data_generator.py', 'r') as f:
        content = f.read()
    
    # Check default parameter
    if 'def generate_patient_data(num_records=3500):' in content:
        print("✅ Default parameter updated to 3500")
    else:
        print("❌ Default parameter not updated")
        return False
    
    # Check save_datasets function
    if 'patient_data = generate_patient_data(3500)' in content:
        print("✅ save_datasets function updated to 3500")
    else:
        print("❌ save_datasets function not updated")
        return False
    
    return True

def check_readme():
    """Check that README.md mentions 3,500 records."""
    print("\n🔍 Checking README.md...")
    
    with open('README.md', 'r') as f:
        content = f.read()
    
    if '3,500 records' in content:
        print("✅ README.md mentions 3,500 records")
    else:
        print("❌ README.md doesn't mention 3,500 records")
        return False
    
    # Check for python3 commands
    if 'python3' in content:
        print("✅ README.md includes python3 commands for Linux")
    else:
        print("❌ README.md missing python3 commands")
        return False
    
    return True

def check_notebook():
    """Check that the Jupyter notebook mentions 3,500 records."""
    print("\n🔍 Checking healthcare_analysis.ipynb...")
    
    with open('healthcare_analysis.ipynb', 'r') as f:
        content = f.read()
    
    # Check for 3,500 in comments
    if '3,500 records' in content:
        print("✅ Notebook mentions 3,500 records in documentation")
    else:
        print("❌ Notebook doesn't mention 3,500 records")
        return False
    
    # Check for 3500 in code
    if 'generate_patient_data(3500)' in content:
        print("✅ Notebook code updated to generate 3500 records")
    else:
        print("❌ Notebook code not updated")
        return False
    
    # Check project summary
    if '3,500 patient records across 20 hospitals' in content:
        print("✅ Project summary updated with correct numbers")
    else:
        print("❌ Project summary not updated")
        return False
    
    return True

def check_file_structure():
    """Check that all required files exist."""
    print("\n🔍 Checking file structure...")
    
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
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            all_exist = False
    
    return all_exist

def check_requirements():
    """Check that requirements.txt has necessary packages."""
    print("\n🔍 Checking requirements.txt...")
    
    with open('requirements.txt', 'r') as f:
        content = f.read().lower()
    
    required_packages = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'jupyter']
    missing = []
    
    for package in required_packages:
        if package in content:
            print(f"✅ {package}")
        else:
            print(f"❌ {package} - MISSING")
            missing.append(package)
    
    return len(missing) == 0

def main():
    """Run all verification checks."""
    print("🏥 Healthcare Analytics Project - Update Verification")
    print("=" * 60)
    
    checks = [
        ("File Structure", check_file_structure),
        ("Data Generator", check_data_generator),
        ("README.md", check_readme),
        ("Jupyter Notebook", check_notebook),
        ("Requirements", check_requirements)
    ]
    
    passed = 0
    total = len(checks)
    
    for name, check_func in checks:
        print(f"\n📋 {name}")
        print("-" * 30)
        if check_func():
            passed += 1
            print(f"✅ {name} - PASSED")
        else:
            print(f"❌ {name} - FAILED")
    
    print("\n" + "=" * 60)
    print(f"📊 VERIFICATION RESULTS: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 ALL UPDATES VERIFIED SUCCESSFULLY!")
        print("\n📋 Project is ready with 3,500 patient records")
        print("📋 Use python3 commands on Linux systems")
        print("📋 All files properly updated and structured")
        return True
    else:
        print("❌ Some verification checks failed")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        exit(1)
