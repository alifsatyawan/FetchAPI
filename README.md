# README

## Project Description

This project implements a RESTful API for managing user points per payer using Python and the Flask web framework. Users can add points, spend points, and fetch their current point balance broken down by payer. The API follows specific rules for spending points, such as spending the oldest points first and ensuring no payer's points go negative.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up the Environment](#setting-up-the-environment)
- [Running the Application](#running-the-application)
- [Testing the API](#testing-the-api)
  - [Add Points Endpoint](#add-points-endpoint)
  - [Spend Points Endpoint](#spend-points-endpoint)
  - [Get Points Balance Endpoint](#get-points-balance-endpoint)
- [Testing with Provided Data](#testing-with-provided-data)
- [Troubleshooting](#troubleshooting)
- [Additional Notes](#additional-notes)
- [Contact](#contact)

## Prerequisites

- **Operating System:** Windows, macOS, or Linux
- **Python 3.x:** The application requires Python 3 to run.
- **Command Line Interface:** Ability to use a terminal or command prompt.
- **Internet Connection:** To download Python and install dependencies.

## Installation

### 1. Install Python 3

#### Windows

1. **Download Python Installer:**
   - Visit [Python's official website](https://www.python.org/downloads/windows/) and download the latest Python 3 installer for Windows.

2. **Run the Installer:**
   - Double-click the downloaded file to run the installer.
   - **Important:** Check the box that says **"Add Python 3.x to PATH"** during installation.
   - Proceed with the installation using the default settings.

#### macOS

1. **Download Python Installer:**
   - Visit [Python's official website](https://www.python.org/downloads/mac-osx/) and download the latest Python 3 installer for macOS.

2. **Run the Installer:**
   - Open the downloaded `.pkg` file and follow the installation prompts.

3. **Alternative via Homebrew:**
   - If you have Homebrew installed, you can install Python by running:
     ```bash
     brew install python
     ```

#### Linux

1. **Using Package Manager:**
   - For Debian/Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install python3 python3-venv python3-pip
     ```
   - For Fedora:
     ```bash
     sudo dnf install python3 python3-venv python3-pip
     ```
   - For CentOS:
     ```bash
     sudo yum install python3 python3-venv python3-pip
     ```

### 2. Verify Python Installation

Open a terminal or command prompt and run:

```bash
python3 --version

## Setting Up the Environment

### 1. Download the Project Files

1. **Create a Project Directory:**

   - Open a terminal or command prompt.
   - Navigate to the directory where you want to store the project.
   - Create a new directory:

     ```bash
     mkdir point_management_api
     cd point_management_api
     ```

2. **Create `app.py` File:**

   - Create a new file named `app.py` in the project directory.
   - Copy the following code into `app.py`:

     ```python
     # (Include the full code here)
     ```

### 2. Set Up a Virtual Environment (Optional but Recommended)

A virtual environment isolates your project's dependencies, ensuring they don't interfere with system-wide packages.

#### Create a Virtual Environment

```bash
python3 -m venv venv


