from kedro.pipeline import node, Pipeline
from sklearn.ensemble import RandomForestClassifier

def train_model(data):
    X = data.drop("Survived", axis=1)
    y = data["Survived"]
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def predict_model(model, data):
    features = data.drop("Survived", axis=1)
    return model.predict(features)

def create_pipeline(**kwargs):
    return Pipeline([
             node(
                func=train_model,
                inputs=["train_proc"],
                outputs="model",
                name="train_titanic"
            ),
            node(
                func=predict_model,
                inputs=["model", "test_proc"],
                outputs="predictions",
                name="predict_model",
            ),
    ])
