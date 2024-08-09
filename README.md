---

# Price Comparison of iPhone XR (64GB) - Yellow on Amazon and Flipkart

Welcome to the Price Comparison Automation project! This project automates the process of comparing the price of an iPhone XR (64GB) - Yellow between two of the largest e-commerce websites in India: **Amazon** and **Flipkart**. The goal is to determine which website offers the iPhone at a lower price and print the result in the console.

## 🚀 Project Overview

This project demonstrates the use of **Selenium WebDriver** with **TestNG** in a **Page Object Model (POM)** framework to perform web automation. The script is written in **Java** and showcases how to:

1. Navigate to Amazon and Flipkart websites.
2. Search for the iPhone XR (64GB) - Yellow.
3. Extract the price of the iPhone on both websites.
4. Compare the prices and determine the cheaper option.
5. Display the result in the console.

## 💡 Key Features

- **Page Object Model (POM)**: This design pattern is implemented to promote reusability, maintainability, and readability of the code.
- **Cross-Site Comparison**: The automation script seamlessly compares prices across Amazon and Flipkart.
- **Selenium WebDriver with TestNG**: Utilizes TestNG for test execution and reporting.

## 🛠️ Technologies Used

- **Language**: Java
- **Framework**: Selenium WebDriver
- **Test Framework**: TestNG
- **Design Pattern**: Page Object Model (POM)

## 📝 Steps to Run the Project

1. **Clone the Repository**: Clone this repository to your local machine using the command:
   ```bash
   git clone https://github.com/yourusername/price-comparison-automation.git
   ```

2. **Set Up the Environment**:
   - Ensure you have Java, Maven, and your preferred IDE (e.g., IntelliJ IDEA, Eclipse) installed.
   - Install the necessary dependencies by running `mvn install` from the command line.

3. **Run the Tests**:
   - Navigate to the `src/test/java` directory.
   - Run the TestNG test file that contains the `comparePricesTest()` method.

4. **View the Result**:
   - The test will execute and the result will be displayed in the console, showing which website offers the iPhone XR at a lower price.

## 📁 Project Structure

```
src
├── main
│   └── java
│       └── pages
│           ├── AmazonPage.java
│           └── FlipkartPage.java
└── test
    └── java
        └── tests
            └── PriceComparisonTest.java
```

- **Pages**: Contains the page object classes for Amazon and Flipkart.
- **Tests**: Contains the test class that compares the prices.

## ⚡ Example Output

```
Amazon Price: ₹53,900
Flipkart Price: ₹54,500
Result: Amazon offers the iPhone XR (64GB) - Yellow at a cheaper price.
```

## 🤝 Contributing

Feel free to contribute by opening a pull request. For major changes, please open an issue first to discuss what you would like to change.


## 📧 Contact

For any queries, please reach out at [aayushkumardev@gmail.com].

---
