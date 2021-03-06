from yowsup.demos.zclient.utils import helper
from yowsup.demos.zclient.utils import downloader

class Message(object):
    def __init__(self, message_entity):
        self.who = helper.get_who_send(message_entity)
        self.who_name = helper.sender_name(message_entity)
        self.conversation = message_entity.getFrom()
        self.message_entity = message_entity
        self.valid = False
        self.message = ""
        self.text = ""
        self.file_path = None
        self.command = None
        self.predicate = None
        
        self.build()
        
    def build(self):
        if helper.is_text_message(self.message_entity):
            self.message = helper.clean_message(self.message_entity)
            self.text = helper.clean_message(self.message_entity)
            self.put_command()
            self.valid = True
        
        elif helper.is_media_message(self.message_entity):
            try:
                self.file_path = downloader.get_file(self.message_entity)
                self.text = self.message_entity.getCaption()
                self.message = self.message_entity.getCaption()
                self.valid = True
            except:
                print("Unsupported media file")
        else:
            print("Unsupported message")
            
    
    """
    These two attributes are just easier ways to identify instructions
    But they are not really needed since you have the whole message
    But I use these a lot so fuck it, lemme be happy
    
    command is what goes right next '!'
    predicate is what goes after the command
    ===================================================================
    """
    def put_command(self):
        self.command = helper.command(self.message_entity)
        self.predicate = helper.predicate(self.message_entity)
        
        
    """
    Logs message node
    """
    def log(self, deep=False):
        helper.log(self)
        
        if deep:
            helper.log(self.message_entity)
