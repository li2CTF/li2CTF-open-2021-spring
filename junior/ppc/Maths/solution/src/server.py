import asyncio
import random

HOST, PORT = '0.0.0.0', 23001
FLAG = "flag{7CP_m47h_w17h_h3lp_0f_py7h0n}"
TASKS_COUNT = 50

class MathsServer(asyncio.Protocol):
    def __init__(self):
        self.loop = asyncio.get_running_loop()
        self.level = 0
        self.work = True
        
    def connection_made(self, transport):
        if not self.work:
            return
        self.peername = transport.get_extra_info('peername')
        print(f"Client \033[032mconnected\033[0m: {self.peername}")
        self.transport = transport
        self.transport.write(b"I send you two numbers - you send me multiplication of these numbers. 10 seconds per task. Ready?\n")
        self.loop.call_later(10, self.timeout)
        self.make_task()

    def data_received(self, data):
        if not self.work:
            return
        data = data.decode().strip()
        if data.isdigit():
            self.check_answer(int(data))
        else:
            self.terminate("Not number!")

    def connection_lost(self, exc=None):
        if not self.work:
            return
        if not self.transport.get_extra_info("open"):
            self.transport.write(b"Unexpected error occured!")
        print(f"Client \033[031maborted\033[0m connection: {self.peername}")
        self.transport.close()

    def make_task(self):
        if not self.work:
            return
        a, b = random.randint(0, 100000), random.randint(0, 100000)
        self.ans = a * b
        self.loop.call_later(10, self.timeout)
        self.transport.write(f"{a}, {b}\n".encode())
        
    def check_answer(self, n):
        if not self.work:
            return
        if n == self.ans:
            self.transport.write(b"Correct\n")
            self.level += 1
            if self.level == TASKS_COUNT:
                self.terminate(FLAG)
            else:
                self.make_task()
        else:
            self.terminate("Wrong answer")

    def timeout(self):
        if not self.work:
            return
        self.terminate("You are too slow!")

    def terminate(self, s):
        if not self.work:
            return
        self.work = False
        self.transport.write(f"\n{s}\n".encode())
        print(f"Connection \033[031mterminated\033[0m with user: {self.peername}. Reason: \033[036m{s if s != FLAG else 'User got flag.'}\033[0m")
        self.transport.close()


async def main(host, port):
    loop = asyncio.get_running_loop()
    server = await loop.create_server(MathsServer, host, port)
    print(f"[\033[032m✅\033[00m]\033[032m Socket server successfuly launched on {port} port!\033[0m")
    print("[\033[034m👨‍\033[0m]\033[034m Server made by \033[035m\033[004m@sultanowskii\033[0m")
    print("[\033[036m📄\033[0m]\033[036m Server logs:\033[0m")
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))