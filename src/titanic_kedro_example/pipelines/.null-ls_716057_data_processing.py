from kedro.pipeline import node, Pipeline

def clean_data(train_raw, test_raw):
    train_cleaned = train_raw.dropna(subset=["Age", "Embarked"])
    test_cleaned = test_raw.dropna(subset=["Age", "Embarked"])
    return train_cleaned, test_cleaned

def process_data(train_data, test_data):
    train_data["Sex"] = train_data["Sex"].map({"male": 0, "female": 1})
    train_data = train_data[["Sex", "Age", "Fare", "Survived"]]

    test_data["Sex"] = test_data["Sex"].map({"male": 0, "female": 1})
    test_data = test_data[["Sex", "Age", "Fare", "Survived"]]
    return train_data, test_data

def create_pipeline(**kwargs):
    return Pipeline([
             node(
                func=clean_data,
                inputs=["train_raw", "test_raw"],
                outputs=["train_cleaned", "test_cleaned"],
                name="clean_data"
            ),
            node(
                func=process_data,
                inputs=["train_cleaned", "test_cleaned"],
                outputs=["train_processed", "test_processed"],
                name="process_data"
            ),
    ])
