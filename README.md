# pokedex
A command-line Pokédex in Python that uses the PokeAPI to fetch and display information about a Pokémon, including its type, Dex number, and description.

# Pokedex

A simple command-line interface (CLI) Pokedex application built in Python. This script fetches data for any Pokémon using the public [PokéAPI](https://pokeapi.co/).

## Description

This program prompts the user to enter the name of a Pokémon. It then connects to the PokéAPI, retrieves the relevant data, and displays key information about the Pokémon directly in the terminal. If the requested Pokémon does not exist, it will return an error message.

## Features

-   Fetches and displays a Pokémon's basic information:
    -   Name
    -   National Pokédex Number
    -   Type(s)
-   Retrieves and displays the Pokémon's official Pokédex description (in English).
-   Cleans the description text for better readability.
-   Provides user-friendly feedback during the search process.

## Requirements

-   Python 3.x
-   `requests` library

## Installation

1.  Make sure you have Python 3 installed on your system.
2.  Install the `requests` library using pip. Open your terminal or command prompt and run the following command:
    ```sh
    pip install requests
    ```

## How to Use

1.  Save the code as a Python file (e.g., `Pokedex.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script with the following command:
    ```sh
    python Pokedex.py
    ```
5.  When prompted, type the name of the Pokémon you want to look up and press Enter. The name is not case-sensitive.
