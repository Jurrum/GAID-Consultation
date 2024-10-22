// frontend/src/chatbot/widgets/RecordWidget.js

import React from "react";

const RecordWidget = (props) => {
  const { actionProvider } = props;

  const handleStartRecording = () => {
    actionProvider.handleAudioResponse();
  };

  return (
    <div style={{ marginTop: "10px" }}>
      <button onClick={handleStartRecording} style={{ padding: "10px 20px", backgroundColor: "#5ccc9d", color: "#fff", border: "none", borderRadius: "5px", cursor: "pointer" }}>
        Start Recording
      </button>
    </div>
  );
};

export default RecordWidget;
