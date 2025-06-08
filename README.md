# Healthcare Analytics: Patient Readmission Analysis

## Project Overview
This project analyzes patient readmission rates and treatment effectiveness across multiple hospitals. It identifies factors that contribute to patient readmissions and provides insights that could help healthcare providers improve patient outcomes and reduce unnecessary readmissions.

## Project Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Git

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/lcabrp/patient_analysis_01.git
   cd patient_analysis_01
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux (Method 1 - Preferred)
   python3 -m venv venv
   source venv/bin/activate

   # On macOS/Linux (Method 2 - If Method 1 fails)
   python3 -m venv venv --without-pip
   source venv/bin/activate
   python3 -m ensurepip --upgrade
   ```

3. Install required dependencies:
   ```bash
   # On Windows
   pip install -r requirements.txt

   # On macOS/Linux
   pip3 install -r requirements.txt
   ```

4. Run the setup script to generate datasets and initialize the database:
   ```bash
   # On Windows
   python setup_project.py

   # On macOS/Linux
   python3 setup_project.py
   ```

5. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

6. Open the `healthcare_analysis.ipynb` notebook to view the analysis.

### What to Expect
After running the setup script, you will have:
- Synthetic patient and hospital datasets in the `./data/` directory
- A SQLite database (`healthcare_database.db`) with the processed data
- All necessary files to run the complete analysis

The main notebook will walk you through:
- Data exploration and cleaning
- Feature engineering
- Database operations with SQL joins
- Statistical analysis
- Three different types of visualizations
- Key insights and recommendations

## Technologies Used
- **Python**: Core programming language for data analysis
- **Pandas**: Used for data cleaning, manipulation, and analysis of patient records
- **SQLite**: Database for storing and querying patient and hospital data
- **Matplotlib/Seaborn**: Created visualizations to identify patterns in readmission rates
- **Jupyter Notebooks**: Provides an interactive environment to present code, visualizations, and analysis

## Data Sources
This project uses two synthetic datasets:
1. **Patient Records**: 3,500 records containing patient demographics, diagnoses, treatments, and readmission information
2. **Hospital Information**: 20 records with details about hospitals, including size, location, and specialties

The datasets are designed to simulate real-world healthcare data patterns while ensuring privacy and compliance. The data dictionary for each dataset is provided in the notebook.

## Project Structure
```
healthcare-analytics/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── setup_project.py            # Setup script to initialize project
├── healthcare_analysis.ipynb   # Main analysis notebook
├── healthcare_database.db      # SQLite database (created after setup)
├── data/                       # Generated datasets
│   ├── patient_data.csv        # Patient records dataset
│   └── hospital_data.csv       # Hospital information dataset
└── src/                        # Source code modules
    ├── __init__.py             # Package initialization
    ├── data_generator.py       # Synthetic data generation
    ├── db_utils.py             # Database utilities
    └── visualization.py        # Plotting functions
```

## Key Features Demonstrated
- **Data Generation**: Creates realistic synthetic healthcare datasets
- **Data Cleaning**: Handles missing values and data type conversions
- **Feature Engineering**: Creates new variables for enhanced analysis
- **Database Integration**: Uses SQLite with proper table relationships
- **SQL Queries**: Complex joins and aggregations for data analysis
- **Visualizations**: Three different chart types with consistent styling
- **Statistical Analysis**: Correlation analysis and risk factor identification
- **Documentation**: Comprehensive comments and markdown explanations

## Troubleshooting

### Virtual Environment Issues
If you encounter issues creating the virtual environment:

1. **Error with `python3 -m venv venv`**:
   ```bash
   # Try without pip first
   python3 -m venv venv --without-pip
   source venv/bin/activate
   python3 -m ensurepip --upgrade
   ```

2. **Alternative: Use system Python** (not recommended for production):
   ```bash
   # Skip virtual environment and install directly
   pip3 install -r requirements.txt
   python3 setup_project.py
   ```

3. **Missing Python packages**:
   ```bash
   # On Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install python3-venv python3-pip

   # On CentOS/RHEL
   sudo yum install python3-venv python3-pip
   ```

### Common Issues
- **ModuleNotFoundError**: Make sure you've activated the virtual environment and installed requirements
- **Permission errors**: Try using `pip3 install --user -r requirements.txt`
- **Jupyter not found**: Install with `pip3 install jupyter notebook`