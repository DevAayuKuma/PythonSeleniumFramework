Project Description:

This Python project utilizes the Page Object Model (POM) design pattern, TestNG testing framework, and Selenium WebDriver for cross-browser automation to compare iPhone XR (64GB) - Yellow prices across Amazon India and Flipkart.

Key Features:

Cross-Browser Compatibility: Supports major browsers like Chrome, Firefox, Edge, etc. (configure in testNG.xml).
Reusable Page Objects: Encapsulates UI elements and actions for maintainability.
Modular TestNG Tests: Clear and concise test definitions using TestNG annotations.
Enhanced Readability: Descriptive variable and method names.
Informative Output: Prints the final comparison result to the console.
Improved Error Handling: Uses try-except blocks to gracefully handle potential exceptions.
Instructions:

Clone or Download the Repository:

Bash
git clone https://github.com/your-username/intelligent-price-comparison.git
Use code with caution.

Install Dependencies:

Bash
pip install selenium webdriver-manager testng
Use code with caution.

Configure Browser Drivers (if needed):
Download the appropriate browser driver (e.g., ChromeDriver) from https://chromedriver.chromium.org/ and place it in the project directory or a location specified in your system's PATH environment variable.

Run Tests:

Bash
pytest test_price_comparison.py
Use code with caution.

Getting Started with Page Object Model:

This project demonstrates the Page Object Model (POM) for effective UI element interactions and reusability:

Create separate classes for each web page with its elements and actions encapsulated.
Access page objects from your test classes for a clean separation of concerns.
Test Execution and Comparison Logic:

Open Amazon and Flipkart websites using WebDriver.
Search for "iPhone XR (64GB) - Yellow" on both platforms.
Select the matching iPhone on each website.
Extract the iPhone's price from the product page using appropriate selectors.
Compare the extracted prices using conditional statements.
Print the website offering the iPhone at a lower price.
Handle potential exceptions (e.g., product not found) using try-except blocks.
Contribution and Improvements:

Feel free to fork the repository, experiment with different POM implementations, or enhance the code for advanced test automation scenarios.

Disclaimer:
This code is provided for educational purposes only.
