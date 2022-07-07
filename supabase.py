import os
import requests
import datetime

def telegram_temporary_code(temporary_code, chat_id):
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    end_point = 'rest/v1/temp_codes'
    url = supabase_url + end_point
    date = datetime.datetime.now() + datetime.timedelta(minutes=10)
    
    headers = {
                'apikey': supabase_key, 
                'Content-Type': "application/json", 
                'Prefer': "return=representation"
              }
    
    data = {
                'telegram': chat_id, 
                'code': temporary_code, 
                'valid_until': str(date)
            }

    params = {"telegram": "eq." + str(chat_id)}
    delete_temporary_code_request = requests.delete(url, params=params, headers=headers)
    post_temporary_code_request = requests.post(url, json=data, headers=headers)
    
    if (delete_temporary_code_request.status_code != 200):
        status_code = delete_temporary_code_request.status_code
        return ("Bad DELETE request temporary code. Http status code: " + str(status_code))
    if (post_temporary_code_request.status_code != 201):
        status_code = post_temporary_code_request.status_code
        return ("Bad POST request temporary code. Http status code: " + str(status_code))
        
    return 0
    
    