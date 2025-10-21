document.getElementById("send-btn").onclick = async function() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;
    addUserMessage(userInput);
    document.getElementById("user-input").value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: userInput})
    });
    const data = await response.json();

    addBotMessage(data.nlp_response);
    addAITip(data.synthetic_advice);
};

function addUserMessage(text) {
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += "<div class='user-bubble'>" + text + "</div>";
    chatbox.scrollTop = chatbox.scrollHeight;
}
function addBotMessage(text) {
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += "<div class='bot-bubble'>" + text + "</div>";
    chatbox.scrollTop = chatbox.scrollHeight;
}
function addAITip(text) {
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += "<div class='ai-tip'>AI Tip: " + text + "</div>";
    chatbox.scrollTop = chatbox.scrollHeight;
}
