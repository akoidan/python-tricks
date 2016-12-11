import tornado.ioloop
import tornado.web
from tornado.websocket import WebSocketHandler

html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
	<style>
		pre {
			max-height: calc( 100vh - 60px);
			overflow-y: auto;
		}
	</style>
	<script>

		function doPost(data) {
			var r = new XMLHttpRequest();
			/*Firefox doesn't accept null*/
			r.onreadystatechange = function () {
				if (r.readyState === 4 && r.status === 200) {
					var pre = document.getElementById('pre');
					pre.textContent = pre.textContent + new Date().getMinutes() + ":" + new Date().getSeconds() +'>>'+r.responseText+'\\n';
					pre.scrollTop = pre.scrollHeight
				}
			};
			r.open("POST", '');
			r.send(data);
		}

		function doSubmit() {
			window.event.preventDefault();
			doPost(document.getElementById('message').value)
		}
	</script>
</head>
<body>
<form method="post" onsubmit="doSubmit()">
	<input type="text" value="message" id="message" required>
	<input type="submit" value="send">
</form>
<pre id="pre">
</pre>
</body>
</html>
"""
wsHandlers = []


class MainHandler(WebSocketHandler):

    def post(self):
        for handler in wsHandlers:
            handler.write_message(self.request.body)
        self.write('{}: "{}"'.format(len(wsHandlers), self.request.body))

    def get(self):
        self.write(html)

    def open(self):
        wsHandlers.append(self)
        print('opened new connection')
        self.write_message('asdas')

    def on_close(self):
        wsHandlers.remove(self)
        print('closed new connection')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(9999)
    print('http://localhost:9999')
    tornado.ioloop.IOLoop.current().start()

