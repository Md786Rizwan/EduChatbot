document.getElementById("send-btn").onclick = async function() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;
    addMessage("You: " + userInput);
    document.getElementById("user-input").value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: userInput})
    });
    const data = await response.json();

    addMessage("Counselor: " + data.nlp_response);
    addMessage("AI Tip: " + data.synthetic_advice);
};

function addMessage(text) {
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += "<div>"+text+"</div>";
    chatbox.scrollTop = chatbox.scrollHeight;
}
