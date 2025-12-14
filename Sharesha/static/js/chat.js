let currentMode = "academic";

// Auto-scroll function - scrolls the chat-window container
function scrollToBottom() {
    const chatWindow = document.querySelector(".chat-window");
    if (chatWindow) {
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
}

function setMode(mode) {
    currentMode = mode;

    // Update button styles
    document.querySelectorAll(".mode-btn").forEach(btn =>
        btn.classList.remove("active")
    );
    document.querySelector(`.mode-btn.${mode}`).classList.add("active");

    // Update main avatar image and name
    const avatarImg = document.getElementById("avatar-img");
    const avatarName = document.getElementById("avatar-name");

    if (mode === "academic") {
        avatarImg.src = "/static/images/academic_avatar.png";
        avatarImg.style.borderColor = "#6a857f";
        avatarName.textContent = "Gandalf";
        avatarName.style.background = "linear-gradient(90deg, #b4c8c3, #9bb0ab)";
        avatarName.style.webkitBackgroundClip = "text";
        avatarName.style.backgroundClip = "text";
    } else {
        avatarImg.src = "/static/images/personal_avatar.png";
        avatarImg.style.borderColor = "#7a8e88";
        avatarName.textContent = "Samwise";
        avatarName.style.background = "linear-gradient(90deg, #9bb0ab, #7a8e88)";
        avatarName.style.webkitBackgroundClip = "text";
        avatarName.style.backgroundClip = "text";
    }
    
    // CLEAR ALL PREVIOUS CHAT MESSAGES
    const chat = document.getElementById("chat-messages");
    chat.innerHTML = '';  // Clear everything
    
    // Add only mode switch message
    const modeMsg = document.createElement("div");
    modeMsg.className = "message bot-message";
    modeMsg.textContent = `Switched to ${mode.charAt(0).toUpperCase() + mode.slice(1)} mode!`;
    chat.appendChild(modeMsg);
    
    // Auto-scroll after mode change
    scrollToBottom();
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;

    addUserMessage(message);
    input.value = "";
    
    // Show typing indicator
    showTyping();

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, mode: currentMode })
    })
    .then(res => res.json())
    .then(data => {
        // Hide typing indicator
        hideTyping();
        addBotMessage(data.response);
    })
    .catch(error => {
        hideTyping();
        addBotMessage("Sorry, something went wrong. Please try again.");
        console.error('Error:', error);
    });
}

function handleKeyPress(e) {
    if (e.key === "Enter") sendMessage();
}

function addUserMessage(text) {
    const chat = document.getElementById("chat-messages");
    
    // Remove welcome message if it exists
    const welcomeMsg = document.querySelector(".welcome-message");
    if (welcomeMsg) {
        welcomeMsg.remove();
    }
    
    const div = document.createElement("div");
    div.className = "message user-message";
    div.textContent = text;
    chat.appendChild(div);
    
    // Auto-scroll after adding user message
    scrollToBottom();
}

function addBotMessage(text) {
    const chat = document.getElementById("chat-messages");
    const div = document.createElement("div");
    div.className = "message bot-message";
    div.textContent = text;
    chat.appendChild(div);
    
    // Auto-scroll after adding bot message
    scrollToBottom();
}

function showTyping() {
    const typingIndicator = document.getElementById("typing");
    if (typingIndicator) {
        typingIndicator.style.display = "flex";
        scrollToBottom();
    }
}

function hideTyping() {
    const typingIndicator = document.getElementById("typing");
    if (typingIndicator) {
        typingIndicator.style.display = "none";
    }
}

// Initialize on page load
window.addEventListener('load', function() {
    scrollToBottom();
});