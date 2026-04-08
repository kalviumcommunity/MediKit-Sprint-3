#!/usr/bin/env python3
"""
Creating a Project Folder Structure for Data Science Work

This script demonstrates best practices for organizing a data science project.
A well-structured project makes collaboration easier and maintains code clarity.
"""

import os
from pathlib import Path


def create_project_structure(project_name):
    """
    Create a standardized project folder structure for data science work.
    
    This structure helps organize:
    - Raw data
    - Processed data
    - Scripts and analysis
    - Outputs and results
    - Documentation
    
    Args:
        project_name (str): Name of the project
    """
    
    # Define the main project directory
    project_root = Path(project_name)
    
    # Define folder structure
    folders = [
        # Data folders
        "data/raw",                    # Original, immutable data
        "data/processed",              # Cleaned and transformed data
        "data/external",               # Data from external sources
        
        # Code folders
        "src",                         # Source code and scripts
        "src/scripts",                 # Data processing scripts
        "src/analysis",                # Analysis scripts
        
        # Output folders
        "output",                      # Generated outputs
        "output/figures",              # Plots and visualizations
        "output/reports",              # Analysis reports
        
        # Documentation folders
        "docs",                        # Project documentation
        "notebooks",                   # Jupyter notebooks for exploration
        
        # Configuration and metadata
        "config",                      # Configuration files
        "logs",                        # Log files
    ]
    
    # Create all folders
    for folder in folders:
        folder_path = project_root / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created folder: {folder}")
    
    # Create important placeholder files
    files = {
        ".gitignore": "# Ignore data files\n/data/raw/*\n/data/processed/*\n*.pyc\n__pycache__/\n",
        "README.md": f"# {project_name}\n\nProject description goes here.\n",
        "requirements.txt": "# Python dependencies\npandas==2.0.0\nnumpy==1.24.0\nmatplotlib==3.7.0\nscipy==1.10.0\n",
    }
    
    for file_name, content in files.items():
        file_path = project_root / file_name
        if not file_path.exists():
            file_path.write_text(content)
            print(f"✓ Created file: {file_name}")
    
    print(f"\n✓ Project structure created successfully!")
    print(f"✓ Navigate to: {project_name}/")


def print_folder_structure(path="."):
    """
    Print the folder structure in a tree-like format.
    
    This helps visualize the organization of the project.
    """
    print("\nProject Folder Structure:")
    print("=" * 50)
    
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = " " * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        subindent = " " * 2 * (level + 1)
        for file in files[:3]:  # Show first 3 files
            print(f"{subindent}{file}")
        
        if len(files) > 3:
            print(f"{subindent}... and {len(files) - 3} more files")


# Folder Structure Explanation
"""
RECOMMENDED STRUCTURE FOR DATA SCIENCE PROJECTS:

project_name/
│
├── data/
│   ├── raw/                 # Original data (never modify)
│   ├── processed/           # Cleaned, transformed data
│   └── external/            # Data from external sources
│
├── src/                     # Source code
│   ├── scripts/             # Data processing and utilities
│   └── analysis/            # Analysis notebooks and scripts
│
├── output/                  # Generated outputs
│   ├── figures/             # Plots, charts, visualizations
│   └── reports/             # Analysis reports, summaries
│
├── docs/                    # Documentation
│   └── README files
│
├── notebooks/               # Jupyter notebooks for exploration
│
├── config/                  # Configuration files
│
├── logs/                    # Log files
│
├── .gitignore              # Files to ignore in version control
├── README.md               # Project overview
├── requirements.txt        # Python package dependencies
└── setup.py                # Project setup configuration
"""


if __name__ == "__main__":
    # Example: Create a new data science project
    project_name = "my_data_science_project"
    
    print("Creating Data Science Project Structure")
    print("=" * 50)
    
    # Create the project structure
    create_project_structure(project_name)
    
    # Optional: Display the structure
    print_folder_structure(project_name)
    
    print("\n" + "=" * 50)
    print("Best Practices:")
    print("- Keep raw data separate and immutable")
    print("- Version control code, not data files")
    print("- Document your data sources")
    print("- Use consistent naming conventions")
    print("- Write scripts to reproduce your analysis")
