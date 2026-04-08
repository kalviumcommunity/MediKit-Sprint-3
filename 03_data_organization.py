#!/usr/bin/env python3
"""
Data Organization: Raw, Processed, and Output Artifacts

This script demonstrates best practices for organizing different types of data
in a data science project: raw data, processed/cleaned data, and output artifacts.
"""

import os
import json
from datetime import datetime
from pathlib import Path


class DataOrganizer:
    """
    Manages organization of raw data, processed data, and outputs.
    
    This class follows best practices:
    - Raw data is never modified (immutable)
    - Processed data is tracked separately
    - Outputs are timestamped and versioned
    """
    
    def __init__(self, project_root="data_project"):
        """
        Initialize the DataOrganizer with folder structure.
        
        Args:
            project_root (str): Root directory of the project
        """
        self.project_root = Path(project_root)
        self.raw_data_dir = self.project_root / "data" / "raw"
        self.processed_data_dir = self.project_root / "data" / "processed"
        self.output_dir = self.project_root / "output"
        
        self._create_directories()
    
    def _create_directories(self):
        """Create the necessary directory structure."""
        self.raw_data_dir.mkdir(parents=True, exist_ok=True)
        self.processed_data_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        print(f"✓ Directories created at: {self.project_root}")
    
    def store_raw_data(self, filename, data):
        """
        Store raw data (immutable).
        
        Raw data should never be modified directly. Always create
        a new processed version instead.
        
        Args:
            filename (str): Name of the raw data file
            data (dict or list): Data to store
        """
        filepath = self.raw_data_dir / filename
        
        # Mark raw data file
        base_name = filename.split('.')[0]
        versioned_name = f"{base_name}_v1.0.json"
        versioned_path = self.raw_data_dir / versioned_name
        
        with open(versioned_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✓ Raw data stored: {versioned_path}")
        return versioned_path
    
    def store_processed_data(self, filename, data, description=""):
        """
        Store processed/cleaned data with metadata.
        
        Processed data includes transformations, cleaning, and
        feature engineering applied to raw data.
        
        Args:
            filename (str): Name of the processed data file
            data (dict or list): Processed data
            description (str): Description of processing steps
        """
        filepath = self.processed_data_dir / filename
        
        # Add timestamp and metadata
        timestamp = datetime.now().isoformat()
        versioned_name = f"{filename.split('.')[0]}_processed_{timestamp.split('T')[0]}.json"
        versioned_path = self.processed_data_dir / versioned_name
        
        # Create metadata file
        metadata = {
            "processed_date": timestamp,
            "description": description,
            "source": "raw data transformation",
        }
        
        # Combine data with metadata
        output = {
            "metadata": metadata,
            "data": data
        }
        
        with open(versioned_path, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"✓ Processed data stored: {versioned_path}")
        return versioned_path
    
    def save_output_artifact(self, artifact_name, content, artifact_type="result"):
        """
        Save output artifacts (visualizations, reports, predictions).
        
        Output artifacts are timestamped to track different versions
        of the same output over time.
        
        Args:
            artifact_name (str): Name of the artifact
            content (str or dict): Content to save
            artifact_type (str): Type of artifact (result, plot, report, etc.)
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        versioned_name = f"{artifact_name}_{artifact_type}_{timestamp}.json"
        filepath = self.output_dir / versioned_name
        
        output = {
            "type": artifact_type,
            "created_at": timestamp,
            "content": content
        }
        
        with open(filepath, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"✓ Output artifact saved: {filepath}")
        return filepath
    
    def list_data_files(self):
        """Display all organized data files."""
        print("\n" + "=" * 60)
        print("DATA ORGANIZATION SUMMARY")
        print("=" * 60)
        
        print("\nRaw Data Files (IMMUTABLE):")
        raw_files = list(self.raw_data_dir.glob("*.json"))
        for f in raw_files:
            print(f"  - {f.name}")
        
        print("\nProcessed Data Files:")
        proc_files = list(self.processed_data_dir.glob("*.json"))
        for f in proc_files:
            print(f"  - {f.name}")
        
        print("\nOutput Artifacts:")
        out_files = list(self.output_dir.glob("*.json"))
        for f in out_files:
            print(f"  - {f.name}")


# Data Organization Best Practices
"""
KEY PRINCIPLES:

1. RAW DATA (Never modify):
   - Keep original data exactly as received
   - Use version control for metadata only
   - Document the source and date
   
   Example: /data/raw/customer_data_v1.0.json

2. PROCESSED DATA (Transformed, cleaned):
   - Create a new file for each transformation
   - Include metadata about processing steps
   - Version by date or iteration number
   
   Example: /data/processed/customer_data_processed_2024-04-08.json

3. OUTPUT ARTIFACTS (Results, reports, visualizations):
   - Timestamp all outputs
   - Include metadata about generation
   - Organize by type (plots, reports, predictions)
   
   Example: /output/analysis_result_20240408_143022.json

4. METADATA:
   - Document data sources
   - Track transformation steps
   - Record processing timestamps
   - Include data descriptions
"""


if __name__ == "__main__":
    # Example: Organize data files
    print("Data Organization Demo")
    print("=" * 60)
    
    organizer = DataOrganizer("demo_project")
    
    # Sample raw data
    raw_data = {
        "customers": [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25},
            {"id": 3, "name": "Charlie", "age": 35},
        ]
    }
    
    # Store raw data
    print("\nStoring raw data...")
    organizer.store_raw_data("customers.json", raw_data)
    
    # Process the data (remove sensitive info, add calculations)
    print("\nProcessing raw data...")
    processed_data = {
        "customers": [
            {"id": 1, "age_group": "30-39", "valid": True},
            {"id": 2, "age_group": "20-29", "valid": True},
            {"id": 3, "age_group": "30-39", "valid": True},
        ]
    }
    
    # Store processed data
    organizer.store_processed_data(
        "customers.json",
        processed_data,
        description="Removed PII, added age groups"
    )
    
    # Save analysis output
    print("\nSaving analysis output...")
    analysis_result = {
        "total_customers": 3,
        "average_age": 30,
        "age_distribution": {"20-29": 1, "30-39": 2}
    }
    organizer.save_output_artifact("customer_analysis", analysis_result, "report")
    
    # List all organized data
    organizer.list_data_files()
