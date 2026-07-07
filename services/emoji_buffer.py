class EmojiBuffer: 

    def __init__(self): 
        self._buffer = [] 

    def add(self, emoji): 
        self._buffer.append(emoji) 

    def clear(self): 
        self._buffer.clear() 

    def undo(self): 
        if self._buffer: 
            self._buffer.pop() 

    def get_display_text(self): 
        return " ".join(self._buffer) 
    
    def get_buffer(self): 
        return self._buffer.copy() 
        
emoji_buffer = EmojiBuffer() 