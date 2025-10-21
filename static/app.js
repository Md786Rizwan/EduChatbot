document.getElementById("send-btn").onclick = async function() {
  const userInput = document.getElementById("user-input").value;
  if (!userInput.trim()) return;
  addMessage("You: " + userInput, true);
  const response = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: userInput})
  });
  const data = await response.json();
  addMessage("Bot: " + data.response, false);
};

function addMessage(message, fromUser) {
  const chatbox = document.getElementById("chatbox");
  const msgDiv = document.createElement("div");
  msgDiv.textContent = message;
  msgDiv.className = fromUser ? "user-msg" : "bot-msg";
  chatbox.appendChild(msgDiv);
  chatbox.scrollTop = chatbox.scrollHeight;
}
