# Excel-Data-Cleaning


## Overview

This project consists of a set of scripts designed to clean and process Excel data. The provided code is a segment of a larger project focused on data preparation tasks. Please note that the code provided here represents only a portion of the entire data cleaning pipeline.

## Description

The scripts contained in this repository are aimed at cleaning and preparing Excel data for further analysis or processing. Below is an overview of the main steps involved:

1. **Stripping and Lowercasing**: Initially, all cells in the Excel file are stripped of leading and trailing spaces, and their contents are converted to lowercase. This step ensures uniformity and consistency in the data.

2. **Handling Multiple Rows**: In the dataset, certain cells contain multiple rows concatenated into a single cell, which may impede analysis. To enhance data granularity and accuracy, the script identifies and removes rows containing the term "unknown" before separating the remaining rows into individual entries.

3. **Data Merging**: After cleaning and separating the rows, the script merges the data into a cohesive format, creating a final Excel file ready for analysis or further processing.

## Data Sample

The data used in this project is a sample consisting of 1000 rows from an Excel file. It's important to note that this dataset is for demonstration purposes only and may not reflect real-world data accurately.

## Usage

To use these scripts, follow these steps:

1. Clone this repository to your local machine.
2. Ensure that Python and the required dependencies are installed.
3. Execute the scripts in the order specified above, providing the necessary input data.

## Dependencies

The following dependencies are required to run the scripts:

- Python (version 3.11)
- Pandas (version 1.5.3)
- Openpyxl (version 3.1.2)
