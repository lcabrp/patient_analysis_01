#!/usr/bin/env python3
"""
Simple test script that doesn't require external packages.
Tests basic project structure and code syntax.
"""

import os
import sys
import ast

def test_project_structure():
    """Test that all required files exist."""
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
    
    print("✓ All required files exist")
    return True

def test_python_syntax():
    """Test that Python files have valid syntax."""
    print("🧪 Testing Python file syntax...")
    
    python_files = [
        'setup_project.py',
        'test_project.py',
        'src/__init__.py',
        'src/data_generator.py',
        'src/db_utils.py',
        'src/visualization.py'
    ]
    
    for file_path in python_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                ast.parse(content)
                print(f"✓ {file_path} - syntax OK")
            except SyntaxError as e:
                print(f"❌ {file_path} - syntax error: {e}")
                return False
        else:
            print(f"⚠️ {file_path} - file not found")
    
    return True

def test_dataset_size_updates():
    """Test that dataset size was updated correctly."""
    print("🧪 Testing dataset size updates...")
    
    # Check data_generator.py
    with open('src/data_generator.py', 'r') as f:
        content = f.read()
        if 'num_records=3500' in content:
            print("✓ data_generator.py updated to 3500 records")
        else:
            print("❌ data_generator.py not updated to 3500 records")
            return False
    
    # Check README.md
    with open('README.md', 'r') as f:
        content = f.read()
        if '3,500 records' in content:
            print("✓ README.md updated to 3,500 records")
        else:
            print("❌ README.md not updated to 3,500 records")
            return False
    
    # Check notebook
    with open('healthcare_analysis.ipynb', 'r') as f:
        content = f.read()
        if '3,500' in content and '3500' in content:
            print("✓ Jupyter notebook updated to 3,500 records")
        else:
            print("❌ Jupyter notebook not updated to 3,500 records")
            return False
    
    return True

def test_requirements_file():
    """Test that requirements.txt has the necessary packages."""
    print("🧪 Testing requirements.txt...")
    
    required_packages = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'jupyter']
    
    with open('requirements.txt', 'r') as f:
        content = f.read().lower()
        
    missing_packages = []
    for package in required_packages:
        if package not in content:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages in requirements.txt: {missing_packages}")
        return False
    
    print("✓ All required packages listed in requirements.txt")
    return True

def main():
    """Run all tests."""
    print("🏥 Healthcare Analytics Project - Simple Test Suite")
    print("=" * 60)
    
    tests = [
        test_project_structure,
        test_python_syntax,
        test_dataset_size_updates,
        test_requirements_file
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()  # Add spacing between tests
    
    print("=" * 60)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Project structure is correct.")
        print("\n📋 Next steps:")
        print("1. Install required packages: pip install -r requirements.txt")
        print("2. Run setup script: python setup_project.py")
        print("3. Open Jupyter notebook: jupyter notebook healthcare_analysis.ipynb")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
