use churn;
INSERT INTO Customers (customerID, gender, SeniorCitizen, Partner, Dependents, tenure)
SELECT DISTINCT
    customerID,
    gender,
    SeniorCitizen,
    Partner,
    Dependents,
    tenure
FROM raw_churn_data;
INSERT INTO Services (customerID, PhoneService, MultipleLines, InternetService,
                      OnlineSecurity, OnlineBackup, DeviceProtection,
                      TechSupport, StreamingTV, StreamingMovies)
SELECT DISTINCT
    customerID,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies
FROM raw_churn_data;
INSERT INTO Contracts (customerID, Contract, PaperlessBilling, PaymentMethod)
SELECT DISTINCT
    customerID,
    Contract,
    PaperlessBilling,
    PaymentMethod
FROM raw_churn_data;
INSERT INTO Billing (customerID, MonthlyCharges, TotalCharges)
SELECT DISTINCT
    customerID,
    MonthlyCharges,
    CAST(TotalCharges AS DECIMAL(10,2))  -- convert from object/string
FROM raw_churn_data;
INSERT INTO Churn (customerID, Churn)
SELECT DISTINCT
    customerID,
    Churn
FROM raw_churn_data;
