class Message():
    def __init__(self, cmd,  source, content):
        self.source = source
        self.content = content
        self.cmd = cmd

    def get_source(self):
        return self.source

    def get_content(self):
        return self.content

    def get_cmd(self):
        return self.cmd

    def get_info(self):
        return self.cmd, self.source, self.content