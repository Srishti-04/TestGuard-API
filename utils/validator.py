def validate_status_code(response, expected=200):
    return response.status_code == expected

def validate_response_time(response, threshold=2):
    return response.elapsed.total_seconds() < threshold