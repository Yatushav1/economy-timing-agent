from fastapi import APIRouter
from app.api.schemas import UserInput
from app.core.timing_engine import evaluate_timing

router = APIRouter()

@router.post("/evaluate")
def evaluate(input_data: UserInput):
    return evaluate_timing(input_data)
