def transform(data):
    data = data.dropna()
    data['processed_flag'] = 1
    return data
