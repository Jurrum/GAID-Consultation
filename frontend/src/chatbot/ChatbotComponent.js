// frontend/src/chatbot/ChatbotComponent.js

import React from "react";
import Chatbot from "react-chatbot-kit";
import "react-chatbot-kit/build/main.css";

import config from "./config";
import ActionProvider from "./ActionProvider";
import MessageParser from "./MessageParser";

const ChatbotComponent = () => {
  return (
    <div style={{ maxWidth: "400px", margin: "0 auto" }}>
      <Chatbot
        config={config}
        messageParser={MessageParser}
        actionProvider={ActionProvider}
      />
    </div>
  );
};

export default ChatbotComponent;
