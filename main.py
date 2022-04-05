from zipcodelib import validator, formatter
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/zipcode/{zipcode_value}/validate")
async def zipcode_validate(zipcode_value: str):
    is_valid = validator.is_valid(zipcode_value)
    if not is_valid:
        raise HTTPException(status_code=400, detail=f"Invalid zipcode {zipcode_value}")

    return {
        "zipcode": f"{zipcode_value}",
        "is_valid": f"{is_valid}"
    }


@app.get("/zipcode/{zipcode_value}/format")
async def zipcode_format(zipcode_value: str):
    try:
        formatted_string = formatter.str_format(zipcode_value)
    except ValueError as value_error:
        raise HTTPException(status_code=400, detail=f"{str(value_error)}")
    return {
        "zipcode": f"{zipcode_value}",
        "formatted_zipcode": f"{formatted_string}"
    }
