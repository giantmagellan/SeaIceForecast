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

To run [main](https://github.com/giantmagellan/SeaIceForecast/blob/main/main.ipynb) and perform analysis, first install and activate the [Pipenv](https://docs.pipenv.org/) virtual environment.

Install Pipenv

``` python -m pip install pipenv ```

Create virtual environment

``` python -m pipenv install ```

To activate the project's virtual environment and it's packages, run ...

``` python -m pipenv shell ```

## Usage

### Run Analysis

Once the virtual environment has been activate, open the [main](https://github.com/giantmagellan/SeaIceForecast/blob/main/main.ipynb) notebook and simply click 'Run all'.  

### End Working Session

``` exit ```