start = {
    'date': 11,
    'hour': 11,
    'minute': 11
}

def sol():

    date, hour, minute = map(int, input().split())

    start_minutes = start['date'] * 24 * 60 + start['hour'] * 60 + start['minute']
    
    input_minutes = date * 24 * 60 + hour * 60 + minute

    counter = input_minutes - start_minutes
    
       
    return counter if counter >= 0 else -1

print(sol())