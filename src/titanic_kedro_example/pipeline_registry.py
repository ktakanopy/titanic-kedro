"""Project pipelines."""
from kedro.pipeline import Pipeline
import titanic_kedro_example.pipelines.data_processing as dp
import titanic_kedro_example.pipelines.data_modeling as mp
from typing import Dict

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipeline.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pl = dp.create_pipeline()
    modeling_pl = mp.create_pipeline()

    return {
        "de": data_processing_pl,
        "ds": modeling_pl,
        "__default__": data_processing_pl + modeling_pl,
    }
