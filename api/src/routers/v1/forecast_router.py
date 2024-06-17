from fastapi import APIRouter, HTTPException, Depends, Query
from matplotlib import pyplot as plt

from api.src.configurations.users import get_user_session
from api.src.schemas.schemas import ForecastSchema


forecast_router = APIRouter(
    tags=['Forecast Service'],
    prefix='/forecast'
)

plt.switch_backend('Agg')

@forecast_router.get("/forecast", response_model=ForecastSchema)
def get_forecast(period: int, user_id: str = Query(...), user_session=Depends(get_user_session)):
    if period < 1 or period > 3:
        raise HTTPException(status_code=400, detail="Invalid period value. Must be 1, 2, or 3")
    
    return user_session['ml_service'].get_forecast(period)