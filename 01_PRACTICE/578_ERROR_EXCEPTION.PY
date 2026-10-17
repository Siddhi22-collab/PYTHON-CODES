def process_data(data):
    try:
        if not data:
            raise ValueError("Input data is empty")

        return {"status": "success", "data": data}

    except ValueError as error:
        return {"status": "error", "message": str(error)}


print(process_data("Medical report text"))
print(process_data(""))