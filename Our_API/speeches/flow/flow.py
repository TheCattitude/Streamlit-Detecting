
from taxifare.interface.main import preprocess, train, evaluate

from prefect import task, Flow, Parameter

import os
import requests

@task
def preprocess_new_data(experiment):
    """
    Run the preprocessing of the new data
    """
    preprocess()
    preprocess(source_type='val')

@task
def evaluate_production_model(status):
    """
    Run the `Production` stage evaluation on new data
    Returns `eval_mae`
    """
    eval_mae = evaluate()
    return eval_mae

@task
def re_train(status):
    """
    Run the training
    Returns train_mae
    """
    train_mae = train()
    return train_mae

@task
def notify(eval_mae, train_mae):
    base_url = 'https://wagon-chat.herokuapp.com'
    channel = 'krokrob'
    url = f"{base_url}/{channel}/messages"
    author = 'krokrob'
    content = "Evaluation MAE: {} - New training MAE: {}".format(
        round(eval_mae, 2), round(train_mae, 2))
    data = dict(author=author, content=content)
    response = requests.post(url, data=data)
    response.raise_for_status()

def build_flow():
    """
    build the prefect workflow for the `taxifare` package
    """
    flow_name = os.environ.get("PREFECT_FLOW_NAME")

    with Flow(flow_name) as flow:

        # retrieve mlfow env params
        mlflow_experiment = os.environ.get("MLFLOW_EXPERIMENT")

        # create workflow parameters
        experiment = Parameter(name="experiment", default=mlflow_experiment)

        # register tasks in the workflow
        status = preprocess_new_data(experiment)
        eval_mae = evaluate_production_model(status)
        train_mae = re_train(status)
        notify(eval_mae, train_mae)

    return flow
