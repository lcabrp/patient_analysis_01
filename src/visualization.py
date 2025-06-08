"""
Visualization utilities for the Healthcare Analytics project.
Contains functions for creating standardized plots.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set consistent styling for all visualizations
def set_plot_style():
    """Set consistent styling for all visualizations."""
    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12
    
    # Use a consistent color palette
    colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6", "#1abc9c"]
    sns.set_palette(sns.color_palette(colors))  # Use a consistent color palette

def plot_readmission_by_diagnosis(data):
    """
    Create bar chart of readmission rates by diagnosis.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing patient data with diagnosis and readmission info
    
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    set_plot_style()
    
    # Calculate readmission rate by diagnosis
    readmission_by_diagnosis = data.groupby('diagnosis')['readmitted'].mean().sort_values(ascending=False)
    
    fig, ax = plt.subplots()
    bars = readmission_by_diagnosis.plot(kind='bar', ax=ax)
    
    # Add percentage labels on top of bars
    for i, v in enumerate(readmission_by_diagnosis):
        ax.text(i, v + 0.01, f"{v:.1%}", ha='center')
    
    plt.title('Readmission Rate by Diagnosis', fontsize=16)
    plt.xlabel('Diagnosis', fontsize=14)
    plt.ylabel('Readmission Rate', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    return fig

def plot_los_vs_readmission(data):
    """
    Create box plot of length of stay vs readmission status.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing patient data with length of stay and readmission info
    
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    set_plot_style()
    
    fig, ax = plt.subplots()
    sns.boxplot(x='readmitted', y='length_of_stay', data=data, ax=ax)
    
    plt.title('Length of Stay vs. Readmission Status', fontsize=16)
    plt.xlabel('Readmitted', fontsize=14)
    plt.ylabel('Length of Stay (days)', fontsize=14)
    plt.xticks([0, 1], ['No', 'Yes'])
    
    # Add statistical annotation
    not_readmitted = data[data['readmitted'] == 0]['length_of_stay'].mean()
    readmitted = data[data['readmitted'] == 1]['length_of_stay'].mean()
    
    plt.annotate(f'Mean: {not_readmitted:.1f} days', xy=(0, not_readmitted), 
                 xytext=(0, not_readmitted + 2), ha='center',
                 arrowprops=dict(arrowstyle='->'))
    
    plt.annotate(f'Mean: {readmitted:.1f} days', xy=(1, readmitted), 
                 xytext=(1, readmitted + 2), ha='center',
                 arrowprops=dict(arrowstyle='->'))
    
    plt.tight_layout()
    return fig

def plot_hospital_performance(data):
    """
    Create scatter plot of hospital quality score vs readmission rate.

    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing joined hospital and patient data

    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    set_plot_style()

    # Calculate readmission rate by hospital
    hospital_stats = data.groupby(['hospital_id', 'quality_score']).agg({
        'readmitted': ['count', 'sum']
    }).reset_index()

    hospital_stats.columns = ['hospital_id', 'quality_score', 'total_patients', 'readmissions']
    hospital_stats['readmission_rate'] = hospital_stats['readmissions'] / hospital_stats['total_patients']

    fig, ax = plt.subplots()

    # Create scatter plot with size based on number of patients
    scatter = ax.scatter(hospital_stats['quality_score'],
                        hospital_stats['readmission_rate'],
                        s=hospital_stats['total_patients'] * 3,  # Size based on patient count
                        alpha=0.6)

    plt.title('Hospital Quality Score vs. Readmission Rate', fontsize=16)
    plt.xlabel('Hospital Quality Score (1-5)', fontsize=14)
    plt.ylabel('Readmission Rate', fontsize=14)

    # Add trend line
    z = np.polyfit(hospital_stats['quality_score'], hospital_stats['readmission_rate'], 1)
    p = np.poly1d(z)
    plt.plot(hospital_stats['quality_score'], p(hospital_stats['quality_score']),
             "r--", alpha=0.8, linewidth=2)

    # Add correlation coefficient
    correlation = hospital_stats['quality_score'].corr(hospital_stats['readmission_rate'])
    plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}',
             transform=ax.transAxes, fontsize=12,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    plt.tight_layout()
    return fig