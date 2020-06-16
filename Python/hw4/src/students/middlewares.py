from time import time

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start = time()

        response = self.get_response(request)

        end = time()

        with open('middleware.log', 'a') as file:
            diff = end - start
            file.write(f'{request.path} {request.method} {diff}\n')
        return response