// frontend/src/chatbot/config.js

import { createChatBotMessage } from "react-chatbot-kit";
import ActionProvider from "./ActionProvider";
import MessageParser from "./MessageParser";
import RecordWidget from "./widgets/RecordWidget";

const config = {
  botName: "PreConsultBot",
  initialMessages: [
    createChatBotMessage("Hello! Let's start your pre-consultation questionnaire.", {
      widget: "recordWidget",
    }),
  ],
  widgets: [
    {
      widgetName: "recordWidget",
      widgetFunc: (props) => <RecordWidget {...props} />,
    },
  ],
  customStyles: {
    botMessageBox: {
      backgroundColor: "#376B7E",
    },
    chatButton: {
      backgroundColor: "#5ccc9d",
    },
  },
  MessageParser: MessageParser,
  ActionProvider: ActionProvider,
};

export default config;
