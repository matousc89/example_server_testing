import math
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus

def job_sum(numbers):
    return sum(numbers)

def job_product(numbers):
    return math.prod(map(float,numbers))

class Handler(BaseHTTPRequestHandler):

    ANSWERS = {
        "sum": job_sum,
        "product": job_product,
    }

    def _set_response(self, code=200):
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        task = parsed_path.path.replace("/", "")
        if task in self.ANSWERS:
            query = parse_qs(parsed_path.query)
            numbers = query.get("numbers", False)
            if numbers:
                try:
                    numbers = list(map(float, numbers[0].split(",")))
                    answer = self.ANSWERS[task](numbers)
                    self._set_response()
                    self.wfile.write("The {} of numbers: {} is {}".format(task, numbers, answer).encode('utf-8'))
                except:
                    self._set_response(400)
                    self.wfile.write("Data not understood".encode("utf-8"))
                return
            self._set_response(400)
            self.wfile.write("No data".encode("utf-8"))
        else:
            self._set_response(400)
            self.wfile.write("Cannot comply".encode("utf-8"))

    def log_request(self, code='-', size='-'):
        if isinstance(code, HTTPStatus):
            code = code.value
        self.log_message('"%s" %s %s',
                         self.requestline, str(code), str(size))


if __name__ == '__main__':
    httpd = HTTPServer(("127.0.0.1", 8000), Handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
