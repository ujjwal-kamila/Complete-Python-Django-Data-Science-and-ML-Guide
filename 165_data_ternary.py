# 165. Example - Data Manipulation using the Ternary Operator

def process_data(data):
    process_data = data if data is not None else []
    return process_data

received_data = None
res=process_data(received_data)
print(res)
