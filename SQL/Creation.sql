use churn;
-- Core customer info
CREATE TABLE Customers (
    customerID        VARCHAR(200) PRIMARY KEY,
    gender            VARCHAR(10),        -- e.g. 'Male', 'Female'
    SeniorCitizen     TINYINT(1),         -- 0 or 1
    Partner           VARCHAR(10),        -- 'Yes' or 'No'
    Dependents        VARCHAR(10),        -- 'Yes' or 'No'
    tenure            INT UNSIGNED        -- number of months
);

-- Services subscribed
CREATE TABLE Services (
    serviceID         INT PRIMARY KEY AUTO_INCREMENT,
    customerID        VARCHAR(200),
    PhoneService      VARCHAR(10),        -- 'Yes' or 'No'
    MultipleLines     VARCHAR(20),        -- 'Yes', 'No', 'No phone service'
    InternetService   VARCHAR(20),        -- 'DSL', 'Fiber optic', 'No'
    OnlineSecurity    VARCHAR(20),        -- 'Yes', 'No', 'No internet service'
    OnlineBackup      VARCHAR(20),
    DeviceProtection  VARCHAR(20),
    TechSupport       VARCHAR(20),
    StreamingTV       VARCHAR(20),
    StreamingMovies   VARCHAR(20),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

-- Contract details
CREATE TABLE Contracts (
    contractID        INT PRIMARY KEY AUTO_INCREMENT,
    customerID        VARCHAR(200),
    Contract          VARCHAR(200),        -- 'Month-to-month', 'One year', 'Two year'
    PaperlessBilling  VARCHAR(10),        -- 'Yes' or 'No'
    PaymentMethod     VARCHAR(100),        -- e.g. 'Electronic check'
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

-- Billing info
CREATE TABLE Billing (
    billingID         INT PRIMARY KEY AUTO_INCREMENT,
    customerID        VARCHAR(200),
    MonthlyCharges    DECIMAL(10,2),
    TotalCharges      DECIMAL(10,2),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);

-- Churn status
CREATE TABLE Churn (
    churnID           INT PRIMARY KEY AUTO_INCREMENT,
    customerID        VARCHAR(200),
    Churn             VARCHAR(10),        -- 'Yes' or 'No'
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
);