"""
Visualization utilities for data analysis projects.
Contains generic functions for creating standardized plots.
"""
from typing import Tuple, Optional, Literal, Union
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set consistent styling for all visualizations
def set_plot_style(
    figsize: Tuple[int, int] = (12, 8),
    font_size: int = 12,
    plot_style: Literal['white', 'dark', 'whitegrid', 'darkgrid', 'ticks'] = 'whitegrid',
    palette: Optional[Union[str, list]] = None
) -> None:
    """
    Set consistent styling for all visualizations.
    
    Parameters:
    -----------
    figsize : tuple, optional
        Figure size as (width, height) in inches
    font_size : int, optional
        Base font size for the plot
    style : str, optional
        Seaborn style name
    palette : list or str, optional
        Color palette to use (defaults to a custom palette)
    """
     # Set the style using set_theme instead of directly setting style
    sns.set_theme(
        style=plot_style,
        palette=palette,
        font_scale=font_size/12  # Convert font_size to scale factor
    )
    plt.rcParams['figure.figsize'] = figsize
    plt.rcParams['font.size'] = font_size
    
    # Use a consistent color palette if not specified
    if palette is None:
        colors = ["#3498db", "#2ecc71", "#e74c3c", "#f39c12", "#9b59b6", "#1abc9c"]
        sns.set_palette(sns.color_palette(colors))
    else:
        sns.set_palette(palette)

def create_bar_chart(data, x_column, y_column, title, xlabel, ylabel, 
                     sort_values=False, ascending=False, percentage=False,
                     horizontal=False, color=None, figsize=None)->None:
    """
    Create a generic bar chart with consistent styling.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the data to plot
    x_column : str
        Column name to use for x-axis categories
    y_column : str
        Column name to use for y-axis values
    title : str
        Chart title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    sort_values : bool, optional
        Whether to sort bars by value
    ascending : bool, optional
        Sort direction if sort_values is True
    percentage : bool, optional
        Whether to format y-axis as percentages
    horizontal : bool, optional
        Whether to create a horizontal bar chart
    color : str or list, optional
        Color(s) for the bars
    figsize : tuple, optional
        Figure size as (width, height) in inches
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    if figsize:
        set_plot_style(figsize=figsize)
    else:
        set_plot_style()
    
    # Prepare data
    if sort_values:
        # Group and calculate mean if needed
        if x_column != y_column:
            plot_data = data.groupby(x_column)[y_column].mean().sort_values(ascending=ascending)
        else:
            plot_data = data[x_column].sort_values(ascending=ascending)
    else:
        if x_column != y_column:
            plot_data = data.groupby(x_column)[y_column].mean()
        else:
            plot_data = data[x_column]
    
    # Create plot
    fig, ax = plt.subplots()
    
    # Choose between vertical and horizontal bar chart
    if horizontal:
        plot_data.plot(kind='barh', ax=ax, color=color)
    else:
        plot_data.plot(kind='bar', ax=ax, color=color)
    
    # Add percentage or value labels on bars
    if horizontal:
        for i, v in enumerate(plot_data):
            if percentage:
                ax.text(v + 0.01, i, f"{v:.1%}", va='center')
            else:
                ax.text(v + 0.01, i, f"{v:.2f}", va='center')
    else:
        for i, v in enumerate(plot_data):
            if percentage:
                ax.text(i, v + 0.01, f"{v:.1%}", ha='center')
            else:
                ax.text(i, v + 0.01, f"{v:.2f}", ha='center')
    
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    if not horizontal:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    return fig

def create_box_plot(data, x_column, y_column, title, xlabel, ylabel, 
                    x_labels=None, annotate_means=False, color=None,
                    figsize=None):
    """
    Create a generic box plot with consistent styling.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the data to plot
    x_column : str
        Column name to use for x-axis categories
    y_column : str
        Column name to use for y-axis values
    title : str
        Chart title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    x_labels : list, optional
        Custom labels for x-axis categories
    annotate_means : bool, optional
        Whether to annotate mean values on the plot
    color : str or list, optional
        Color(s) for the boxes
    figsize : tuple, optional
        Figure size as (width, height) in inches
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    if figsize:
        set_plot_style(figsize=figsize)
    else:
        set_plot_style()
    
    fig, ax = plt.subplots()
    sns.boxplot(x=x_column, y=y_column, data=data, ax=ax, palette=color)
    
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    if x_labels:
        plt.xticks(range(len(x_labels)), x_labels)
    
    # Add statistical annotation if requested
    if annotate_means:
        categories = data[x_column].unique()
        
        for i, category in enumerate(categories):
            mean_val = data[data[x_column] == category][y_column].mean()
            
            plt.annotate(f'Mean: {mean_val:.1f}', xy=(i, mean_val), 
                         xytext=(i, mean_val + 2), ha='center',
                         arrowprops=dict(arrowstyle='->'))
    
    plt.tight_layout()
    return fig

def create_scatter_plot(data, x_column, y_column, size_column=None, color_column=None,
                        title=None, xlabel=None, ylabel=None, add_trendline=False, 
                        annotate_correlation=False, figsize=None):
    """
    Create a generic scatter plot with consistent styling.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the data to plot
    x_column : str
        Column name to use for x-axis
    y_column : str
        Column name to use for y-axis
    size_column : str, optional
        Column name to use for point sizes
    color_column : str, optional
        Column name to use for point colors (categorical)
    title : str, optional
        Chart title (defaults to "Y vs X")
    xlabel : str, optional
        X-axis label (defaults to x_column)
    ylabel : str, optional
        Y-axis label (defaults to y_column)
    add_trendline : bool, optional
        Whether to add a trend line
    annotate_correlation : bool, optional
        Whether to annotate correlation coefficient
    figsize : tuple, optional
        Figure size as (width, height) in inches
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    if figsize:
        set_plot_style(figsize=figsize)
    else:
        set_plot_style()
    
    # Set default labels if not provided
    if title is None:
        title = f'{y_column} vs. {x_column}'
    if xlabel is None:
        xlabel = x_column
    if ylabel is None:
        ylabel = y_column
    
    fig, ax = plt.subplots()
    
    # Create scatter plot with optional size and color parameters
    if color_column and size_column:
        categories = data[color_column].unique()
        for category in categories:
            subset = data[data[color_column] == category]
            ax.scatter(subset[x_column], subset[y_column], 
                      s=subset[size_column] * 3,
                      alpha=0.6, label=category)
        plt.legend(title=color_column)
    elif color_column:
        categories = data[color_column].unique()
        for category in categories:
            subset = data[data[color_column] == category]
            ax.scatter(subset[x_column], subset[y_column], alpha=0.6, label=category)
        plt.legend(title=color_column)
    elif size_column:
        scatter = ax.scatter(data[x_column], data[y_column],
                           s=data[size_column] * 3,  # Scale size for visibility
                           alpha=0.6)
    else:
        scatter = ax.scatter(data[x_column], data[y_column], alpha=0.6)
    
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    # Add trend line if requested
    if add_trendline:
        z = np.polyfit(data[x_column], data[y_column], 1)
        p = np.poly1d(z)
        plt.plot(data[x_column], p(data[x_column]), "r--", alpha=0.8, linewidth=2)
    
    # Add correlation coefficient if requested
    if annotate_correlation:
        correlation = data[x_column].corr(data[y_column])
        plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}',
                 transform=ax.transAxes, fontsize=12,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    return fig

def create_line_plot(data, x_column, y_columns, title, xlabel, ylabel, 
                     include_points=True, add_legend=True, figsize=None):
    """
    Create a line plot with multiple series.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the data to plot
    x_column : str
        Column name to use for x-axis
    y_columns : list
        List of column names to plot as separate lines
    title : str
        Chart title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    include_points : bool, optional
        Whether to show data points on the lines
    add_legend : bool, optional
        Whether to add a legend
    figsize : tuple, optional
        Figure size as (width, height) in inches
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    if figsize:
        set_plot_style(figsize=figsize)
    else:
        set_plot_style()
    
    fig, ax = plt.subplots()
    
    for column in y_columns:
        if include_points:
            ax.plot(data[x_column], data[column], 'o-', label=column)
        else:
            ax.plot(data[x_column], data[column], label=column)
    
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    if add_legend:
        plt.legend()
    
    plt.tight_layout()
    return fig

def create_heatmap(data, title=None, cmap="YlGnBu", annot=True, fmt=".2f", 
                   linewidths=0.5, figsize=None):
    """
    Create a heatmap from a correlation matrix or other square data.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the data to plot (usually a correlation matrix)
    title : str, optional
        Chart title
    cmap : str, optional
        Colormap name
    annot : bool, optional
        Whether to annotate cells with values
    fmt : str, optional
        Format string for annotations
    linewidths : float, optional
        Width of lines between cells
    figsize : tuple, optional
        Figure size as (width, height) in inches
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    if figsize:
        set_plot_style(figsize=figsize)
    else:
        set_plot_style()
    
    fig, ax = plt.subplots()
    sns.heatmap(data, annot=annot, cmap=cmap, fmt=fmt, linewidths=linewidths, ax=ax)
    
    if title:
        plt.title(title, fontsize=16)
    
    plt.tight_layout()
    return fig

def create_pie_chart(data, labels=None, title=None, autopct='%1.1f%%', 
                     startangle=90, shadow=False, figsize=None):
    """
    Create a pie chart.
    
    Parameters:
    -----------
    data : array-like
        Data values to plot
    labels : list, optional
        Labels for each slice
    title : str, optional
        Chart title
    autopct : str, optional
        Format string for percentage display
    startangle : int, optional
        Starting angle for the first slice
    shadow : bool, optional
        Whether to add a shadow effect
    figsize : tuple, optional
        Figure size as (width, height) in inches
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    if figsize:
        set_plot_style(figsize=figsize)
    else:
        set_plot_style()
    
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct=autopct, startangle=startangle, shadow=shadow)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    
    if title:
        plt.title(title, fontsize=16)
    
    plt.tight_layout()
    return fig

def create_histogram(data, column, bins=10, title=None, xlabel=None, ylabel='Frequency',
                     kde=False, color=None, figsize=None):
    """
    Create a histogram with optional kernel density estimate.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the data to plot
    column : str
        Column name to plot
    bins : int or sequence, optional
        Number of bins or bin edges
    title : str, optional
        Chart title
    xlabel : str, optional
        X-axis label (defaults to column name)
    ylabel : str, optional
        Y-axis label
    kde : bool, optional
        Whether to overlay a kernel density estimate
    color : str, optional
        Color for the histogram
    figsize : tuple, optional
        Figure size as (width, height) in inches
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    if figsize:
        set_plot_style(figsize=figsize)
    else:
        set_plot_style()
    
    if xlabel is None:
        xlabel = column
    
    if title is None:
        title = f'Distribution of {column}'
    
    fig, ax = plt.subplots()
    sns.histplot(data=data, x=column, bins=bins, kde=kde, color=color, ax=ax)
    
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    
    plt.tight_layout()
    return fig

def create_time_series(data, date_column, value_columns, title=None, 
                       xlabel='Date', ylabel=None, figsize=None):
    """
    Create a time series plot with multiple series.
    
    Parameters:
    -----------
    data : pandas.DataFrame
        DataFrame containing the data to plot
    date_column : str
        Column name with dates/times for x-axis
    value_columns : list
        List of column names to plot as separate lines
    title : str, optional
        Chart title
    xlabel : str, optional
        X-axis label
    ylabel : str, optional
        Y-axis label
    figsize : tuple, optional
        Figure size as (width, height) in inches
        
    Returns:
    --------
    matplotlib.figure.Figure
        The created figure object
    """
    if figsize:
        set_plot_style(figsize=figsize)
    else:
        set_plot_style()
    
    # Ensure the date column is datetime type
    if not pd.api.types.is_datetime64_any_dtype(data[date_column]):
        data = data.copy()
        data[date_column] = pd.to_datetime(data[date_column])
    
    fig, ax = plt.subplots()
    
    for column in value_columns:
        ax.plot(data[date_column], data[column], label=column)
    
    if title:
        plt.title(title, fontsize=16)
    
    plt.xlabel(xlabel, fontsize=14)
    
    if ylabel:
        plt.ylabel(ylabel, fontsize=14)
    
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return fig
