// frontend/src/chatbot/MessageParser.js

class MessageParser {
    constructor(actionProvider) {
      this.actionProvider = actionProvider;
    }
  
    parse(message) {
      // For this implementation, parsing is handled via recording
      // So, we don't need to handle text messages
    }
  }
  
  export default MessageParser;
  