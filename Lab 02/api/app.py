import http.server
import socketserver

# Puerto que pide docker
PUERTO = 3000

class MiAPI(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        respuesta = "Hola, soy Charles Rances Esquerre Martos y esta es mi API local"
        self.wfile.write(respuesta.encode("utf-8"))

Handler = MiAPI
with socketserver.TCPServer(("", PUERTO), Handler) as servidor:
    print("Servidor iniciado en el puerto", PUERTO)
    servidor.serve_forever()