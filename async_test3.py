import asyncio
import contextlib
import os
import locale


class SubprocessProtocol(asyncio.SubprocessProtocol):
    def __init__(self):
        self._exited = False
        self._closed_stdout = False
        self._closed_stderr = False

    @property
    def finished(self):
        return self._exited and self._closed_stdout and self._closed_stderr

    def signal_exit(self):
        if not self.finished:
            return
        loop.stop()        

    def pipe_data_received(self, fd, data):
        if fd == 1:
            name = 'stdout'
        elif fd == 2:
            name = 'stderr'
        text = data.decode(locale.getpreferredencoding(False))
        print('Received from {}: {}'.format(name, text.strip()))

    def pipe_connection_lost(self, fd, exc):
        if fd == 1:
            self._closed_stdout = True
        elif fd == 2:
            self._closed_stderr = True
        self.signal_exit()

    def process_exited(self):
        self._exited = True
        self.signal_exit()


if __name__ == "__main__":
    if os.name == 'nt':
        # On Windows, the ProactorEventLoop is necessary to listen on pipes
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()
    with contextlib.closing(loop):
        # This will only connect to the process
        transport = loop.run_until_complete(loop.subprocess_exec(
            # SubprocessProtocol, 'python', 'run_training.py'))[0]
            SubprocessProtocol, 'python', 'simpletextgenerator/mock/mock_run_training.py'))[0]
            # SubprocessProtocol, 'python', 'async_target.py'))[0]
            # SubprocessProtocol, 'python', '-c', 'print(\'Hello async world!\')'))[0]
        # Wait until process has finished
        loop.run_forever()
        print('Program exited with: {}'.format(transport.get_returncode()))
