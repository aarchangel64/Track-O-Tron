import asyncio


class DataServer:
    """
    A class for sending data over the network (via TCP).
    Listens to incoming TCP request and responds with data from data_fun.

        Attributes:
            host (string): The IP address to host the server on (probably the address of this machine)
            port (int): Which network port to listen for requests on.
            data_fun (function): The function called for retrieving what data to send.
    """

    def __init__(self, host, port, data_fun):
        self.data_fun = data_fun
        self.host = host
        self.port = port

    async def handle_client(self, reader, writer):
        """Handles incoming client TCP requests.

        :param reader:
        :param writer:
        :returns: None
        """
        request = None
        while request != "quit\n":
            request = (await reader.read(255)).decode("utf8")
            response = str(self.data_fun()) + "\n"
            print("Request: " + repr(request))
            print("Response: " + repr(response))
            writer.write(response.encode("utf8"))
            await writer.drain()

        writer.write("Closing connection!".encode("utf8"))
        await writer.drain()
        writer.close()

    async def run_server(self):
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        async with server:
            await server.serve_forever()
