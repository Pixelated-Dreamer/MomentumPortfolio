# Momentum Portfolio Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.24.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A **Streamlit** web application that allows users to analyze stock performance by displaying OHLC (Open, High, Low, Close) data and calculating the 5-month growth rates for up to 5 stocks simultaneously.

## Features

- **Real-time Stock Data**: Fetches live stock data using the `yfinance` library.
- **Interactive UI**: User-friendly interface for entering stock tickers and selecting date ranges.
- **Side-by-Side Comparison**: Displays data for multiple stocks in a clear, organized manner.
- **Growth Rate Calculation**: Calculates and displays the 5-month growth rate for each stock.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Display](#data-display)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/momentum_portfolio.git
   cd momentum_portfolio
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run momentum_portfolio.py
   ```

2. **Open your web browser** and go to `http://localhost:8501`.

3. **Enter up to 5 stock tickers** (comma-separated).

4. **Select your desired date range**.

## Data Display

The application shows:
- **Open Price**
- **High Price**
- **Low Price**
- **Close Price**
- **5-Month Growth Rate**

## Requirements

- **Python**: 3.8+
- See `requirements.txt` for package dependencies.

## Contributing

1. **Fork the repository**.
2. **Create your feature branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework.
- [yfinance](https://github.com/ranaroussi/yfinance) for stock data retrieval.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [NumPy](https://numpy.org/) for numerical operations.

---

Feel free to customize the repository URL, license details, and any other sections to better fit your project. This format should make your README more engaging and informative for users and contributors!
