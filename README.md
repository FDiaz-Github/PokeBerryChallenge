# Poke-berries Statistics API

## Introduction
This API is for retrieving and analyzing statistics about various berries from the Poke-API. It has two endpoints: one that returns statistical data in JSON format and another that displays statistics along with a histogram in an HTML page.

## Installation
To set up the project locally, follow these steps:
1. Clone the repository
2. In the root of the project, create and activate a virtual environment
3. Install the required packages:
```
pip install -r requirements.txt
```
4. Configure the .env.example to be a .env file with the URL provided for the API consumption

## Usage
To run the application use:
```
flask run
```

### Endpoints
- `GET /allBerryStats`: Returns statistics about berries in JSON format.
- `GET /allBerryHistogram`: Displays an HTML page with berry statistics and a histogram for the frequencies.


