import os
import json

from pydantic import BaseModel
from http import HTTPStatus

from object_detection import config, utils

from fastapi import FastAPI, Path
from fastapi.responses import RedirectResponse


app = FastAPI(
    title="object_detection",
    description="",
    version="1.0.0",
)


@utils.construct_response
@app.get("/")
async def _index():
    response = {
        'message': HTTPStatus.OK.phrase,
        'status-code': HTTPStatus.OK,
        'data': {}
    }
    config.logger.info(json.dumps(response, indent=2))
    return response


class PredictPayload(BaseModel):
    pass


@utils.construct_response
@app.post("/predict")
async def _predict(payload: PredictPayload):
    pass
