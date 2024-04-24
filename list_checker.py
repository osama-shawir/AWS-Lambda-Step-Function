def lambda_handler(event, context):
    if isinstance(event, list) and all(isinstance(i, (int, float)) for i in event):
        return 1
    else:
        return 0
