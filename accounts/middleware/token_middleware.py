import time

class ProcessViewTimer:
    def __init__(self , get_response):
        self.get_response = get_response
        print(["midlle ware initialized"])
        
    def __call__(self , request):
        start = time.time()        
        response = self.get_response(request)
        duration = time.time() - start
        print(f"Request processed in {duration:.4f} seconds")
        return response