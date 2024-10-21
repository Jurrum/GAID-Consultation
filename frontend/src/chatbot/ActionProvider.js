// frontend/src/chatbot/ActionProvider.js

import axios from 'axios';

class ActionProvider {
  constructor(createChatBotMessage, setStateFunc, createClientMessage) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
    this.createClientMessage = createClientMessage;
    this.mediaRecorder = null;
    this.audioChunks = [];
  }

  async startQuestionnaire() {
    try {
      const response = await axios.post('/api/start_call', {
        patient_id: 1, // Replace with dynamic patient ID as needed
      });
      const firstQuestion = response.data.response;
      this.addBotMessage(firstQuestion);
    } catch (error) {
      this.addBotMessage("Sorry, there was an error starting the questionnaire.");
      console.error(error);
    }
  }

  async handleUserResponse() {
    // Not used in this implementation
  }

  async handleAudioResponse() {
    if (!this.mediaRecorder) {
      await this.initRecorder();
    }

    if (this.mediaRecorder.state === 'inactive') {
      this.mediaRecorder.start();
      this.addBotMessage("Recording... Please speak after the beep.");
      setTimeout(() => {
        this.mediaRecorder.stop();
        this.addBotMessage("Recording stopped. Processing your response...");
      }, 3000); // Record for 3 seconds
    }
  }

  initRecorder = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.mediaRecorder = new MediaRecorder(stream);
      
      this.mediaRecorder.ondataavailable = (event) => {
        this.audioChunks.push(event.data);
      };
      
      this.mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
        this.audioChunks = [];
        
        const formData = new FormData();
        formData.append('file', audioBlob, 'response.wav');
        
        try {
          const response = await axios.post('/api/speech', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });
          
          const nextResponse = response.data.response;
          this.addBotMessage(nextResponse);
        } catch (error) {
          this.addBotMessage("Sorry, there was an error processing your response.");
          console.error(error);
        }
      };
    } catch (error) {
      this.addBotMessage("Sorry, we couldn't access your microphone.");
      console.error(error);
    }
  };

  addBotMessage(message) {
    const botMessage = this.createChatBotMessage(message, {
      widget: "recordWidget",
    });
    this.setState((prevState) => ({
      ...prevState,
      messages: [...prevState.messages, botMessage],
    }));
  }
}

export default ActionProvider;
