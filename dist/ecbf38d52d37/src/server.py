from sync.testserver import sync_testserver
import sys

class SyncServer(sync_testserver.SyncServerRunner):

  def __init__(self):
    super(SyncServer, self).__init__()

  def run_server(self):
    sync_testserver.SyncServerRunner.run_server(self)

if __name__ == '__main__':
  sys.exit(SyncServer().main())

