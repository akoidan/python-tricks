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
			max-height: calc(100vh - 60px);
			overflow-y: auto;
		}
	</style>
	<script>

		function sliceZero(number, count) {
			return String("00" + number).slice(count || -2);
		}

		document.addEventListener("DOMContentLoaded", function () {
			var pre = document.getElementById('pre');
		});
		var ws;
		function doSubmit() {
			window.event.preventDefault();
			ws.send(document.getElementById('message').value);
		}

		function onMessage(message) {
			var data = message.data.substring(1);
			var pref = message.data.indexOf('S') == 0 ? ">>" : "<<";
			var time = sliceZero(new Date().getMinutes()) + ":"+sliceZero(new Date().getSeconds());
			var newMesasge =  time + pref + data + '\n';
			pre.textContent = pre.textContent + newMesasge;
			pre.scrollTop = pre.scrollHeight;
		}
		function openWs() {
			ws = new WebSocket('ws://' + window.location.host + '/ws');
			ws.onmessage = onMessage;
		}
		openWs();
		ws.onclose = function () { setTimeout(openWs, 1000); }
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
androidHandlers = []
serverHandlers = []


class PageHandler(tornado.web.RequestHandler):
    def get(self):
        with open('./lol2.html', 'rb') as f:
            data = f.read()
            self.write(data)
        self.finish()


class ServerHandler(WebSocketHandler):
    def open(self):
        serverHandlers.append(self)
        print('Opened connection for browser')

    def on_close(self):
        serverHandlers.remove(self)
        print('Cpened connection for browser')

    def broadcast(self, message):
        for handler in androidHandlers:
            handler.write_message(message)

    def on_message(self, message):
        self.broadcast(message)
        self.write_message('S{}: "{}"'.format(len(androidHandlers), message))


class AndroidHandler(WebSocketHandler):
    def open(self):
        print('Opened connection for android')
        self.broadcast('Opened connection for android')
        androidHandlers.append(self)

    def on_close(self):
        androidHandlers.remove(self)
        self.broadcast('Closed connection for android')
        print('Closed connection for android')

    def broadcast(self, message):
        for handler in serverHandlers:
            handler.write_message("A"+message)

    def on_message(self, message):
        self.broadcast(message)


def make_app():
    return tornado.web.Application([
        (r"/page", PageHandler),
        (r"/", AndroidHandler),
        (r"/ws", ServerHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(9999)
    print('http://localhost:9999/page')
    tornado.ioloop.IOLoop.current().start()

