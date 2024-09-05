
# Product Matcher: Automated System for Product List Mapping

## Overview
**Product Matcher** is an open-source solution designed to automate the mapping process between internal product lists of retailers and external product lists from suppliers. This tool aims to replace the slow and error-prone manual matching process with an intelligent, automated system that ensures accurate and efficient product matching.

## Problem Statement
Retailers and distributors often face challenges in matching new incoming products from suppliers with their existing inventory. This process is typically manual, time-consuming, and prone to errors, especially when dealing with large datasets containing various product attributes. The goal of **Product Matcher** is to automate this matching process by accurately identifying identical products based on manufacturer, name, and size.

## Features
- **Automated Matching System**: Automatically match external products from suppliers with internal items based on identical manufacturer, product name, and size.
- **User-Friendly Interface**: Optional front-end application using tools such as Streamlit or Gradio for ease of use and interaction.
- **Prompt Engineering**: Utilizes prompt engineering techniques to enhance matching accuracy.
- **Flexible and Extensible**: Designed to be adaptable to various data formats and can be extended with additional matching rules or machine-learning algorithms.

## Getting Started

### Prerequisites
- Python 3.8 or later
- Required Python packages (listed in `requirements.txt`)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/product-matcher.git
   cd product-matcher
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

## Usage

1. **Prepare Your Data**:  
   Ensure you have two CSV files ready: one containing the internal product list and one containing the external product list from suppliers. Place these files in the `data/` directory.

2. **Run the Matching Script**:  
   The main script will process both CSV files and generate an output table that includes all external items with their corresponding mapped internal products. If no match is found, the table will indicate `NULL` for the internal product.
   ```bash
   python main.py --internal data/internal_products.csv --external data/external_products.csv
   ```

3. **Review the Results**:  
   The output will be saved in the `output/` directory. You can review the generated table for matched and unmatched products.

4. **Optional: Launch the Front-End Application**:  
   To provide a user-friendly interface, you can launch the front-end application:
   ```bash
   streamlit run app.py
   ```

## Examples of Product Matches

Here are a few examples to illustrate how **Product Matcher** works:

| External Product Name                    | Internal Product Name                                       | Status       |
|-------------------------------------------|-------------------------------------------------------------|--------------|
| DIET LIPTON GREEN TEA W/ CITRUS 20 OZ     | Lipton Diet Green Tea with Citrus (20oz)                    | Correct Match |
| CH-CHERRY CHS CLAW DANISH 4.25 OZ         | Cloverhill Cherry Cheese Bearclaw Danish (4.25oz)            | Correct Match |
| Hersheys Almond Milk Choco 1.6 oz         | Hersheys Milk Chocolate with Almonds (1.85oz)               | Wrong Match  |
| COOKIE PEANUT BUTTER 2OZ                  | Famous Amos Peanut Butter Cookie (2oz)                      | Wrong Match  |

## Contributing
We welcome contributions from the community! If you have ideas for new features, bug fixes, or enhancements, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your forked repository.
4. Submit a pull request with a detailed explanation of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or need further assistance, please feel free to open an issue or reach out to us at [your-email@example.com](mailto:your-email@example.com).

## Acknowledgments
Special thanks to all contributors and the open-source community for their valuable feedback and suggestions in improving this tool.
