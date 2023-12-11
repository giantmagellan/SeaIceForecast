# Arctic Sea Ice Extent Forecasting

## Description

Sea ice extent is the total region with at least 15% sea ice cover of the Arctic Ocean at a given time (Michon, 2022) and plays a vital role in sunlight reflection, ocean and air temperature regulation, ocean water circulation, and habitat maintenance (Gold, 2021). The objective of this project is to predict sea ice extent for the coming season and to identify external factors that could cause sea ice extent change.

This notebook downloads Sea Ice Index Daily Extent data directly from the National Snow & Ice Data Center (NSIDC) [website](https://noaadata.apps.nsidc.org/NOAA/G02135/seaice_analysis/). 

#### Notes

Avoid sending too many requests by manually reading in the data set once it has been downloaded to the [data/staging](https://github.com/giantmagellan/SeaIceForecast/tree/main/data/staging/) directory. 

## Table of Contents

- [Installation](#installation)
  - [Pre-requisites](#pre-requisites)
- [Usage](#usage)
  - [Run Analysis](#run-analysis)
  - [End Working Session](#end-working-session)

## Installation

### Pre-requisites

To run [main](https://github.com/giantmagellan/SeaIceForecast/blob/main/main.ipynb) and perform analysis, first install (if not already) and activate the [Conda](https://docs.conda.io/projects/conda/en/stable/index.html) virtual environment.

Install Conda

If Conda is not yet installed, please see [Conda Installation](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html)

Create virtual environment from [environment.yml](https://github.com/giantmagellan/SeaIceForecast/blob/main/environment.yml) file

``` conda env create -f environment.yml ```

Activate the virtual environment

``` conda activate seaiceextent ```

## Usage

### Run Analysis

Once the virtual environment has been activate, open the [main](https://github.com/giantmagellan/SeaIceForecast/blob/main/main.ipynb) notebook and simply click 'Run all'.  

### End Working Session

``` conda deactivate ```