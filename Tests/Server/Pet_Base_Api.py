from enum import Enum

class PET_STATUS(Enum):
    available = 1
    pending = 2
    sold = 3


def create_pet(context, data):
    api_request_context = context.request
    response = api_request_context.post("/v2/pet",
                                        # headers=request_headers(),
                                        data=data
                                        )
    assert response.ok
    assert response.status == 200
    return response.json()['id']


def get_pet_by_status(context, status, validate_statuses=False):
    api_request_context = context.request
    query_params = {
        "status": status.name
    }
    response = api_request_context.get("v2/pet/findByStatus", params=query_params)
    assert response.ok
    assert response.status == 200
    if validate_statuses:
        validate_returned_list_statuses(response.json(), status)
    return response.json()


def validate_returned_list_statuses(list, status):
    for item in list:
        assert item['status'] == status.name


def update_pet(context, pet_id, status):
    api_request_context = context.request
    response = api_request_context.post(f"/v2/pet/{pet_id}",
                                        headers=get_request_headers(),
                                        form={"status": status.name}
                                        )
    assert response.ok
    assert response.status == 200


def get_request_headers():
    return {"accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"}
