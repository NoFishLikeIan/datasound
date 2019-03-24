from pyo import Server, Sine

server = Server()
server.setMidiInputDevice(2)  # Change as required
server.boot()

if __name__ == '__main__':
    server.start()
    audio = Sine().out()
    server.gui(locals())
