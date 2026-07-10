/* ==========================================================
   PINGUAAI INSIGHTBOT
   PROFESSIONAL FRONTEND SCRIPT
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    initializeLoader();
    initializeTheme();
    initializeChat();
    initializeVoiceRecognition();
    initializeExport();
    initializeClearChat();
    loadAnalytics();

});

/* ==========================================================
   GLOBAL ELEMENTS
========================================================== */

const chatBox =
    document.getElementById("chatBox");

const userInput =
    document.getElementById("userInput");

const sendBtn =
    document.getElementById("sendBtn");

const typingIndicator =
    document.getElementById("typingIndicator");

const themeToggle =
    document.getElementById("themeToggle");

const voiceBtn =
    document.getElementById("voiceBtn");

const speakBtn =
    document.getElementById("speakBtn");

const exportBtn =
    document.getElementById("exportBtn");

const clearChatBtn =
    document.getElementById("clearChatBtn");

let lastBotResponse = "";

/* ==========================================================
   LOADER
========================================================== */

function initializeLoader() {

    window.addEventListener("load", () => {

        const loader =
            document.getElementById("loader");

        setTimeout(() => {

            loader.style.opacity = "0";

            loader.style.visibility = "hidden";

        }, 1000);
    });
}

/* ==========================================================
   CHAT INITIALIZATION
========================================================== */

function initializeChat() {

    if (sendBtn) {

        sendBtn.addEventListener(
            "click",
            sendMessage
        );
    }

    if (userInput) {

        userInput.addEventListener(
            "keypress",
            function (e) {

                if (e.key === "Enter") {

                    sendMessage();
                }
            }
        );
    }

    document
        .querySelectorAll(".suggestion-btn")
        .forEach(button => {

            button.addEventListener(
                "click",
                () => {

                    userInput.value =
                        button.innerText;

                    sendMessage();
                }
            );
        });
}

/* ==========================================================
   SEND MESSAGE
========================================================== */

async function sendMessage() {

    const message =
        userInput.value.trim();

    if (!message) {

        showToast(
            "Please enter a question."
        );

        return;
    }

    addUserMessage(message);

    userInput.value = "";

    showTyping();

    try {

        const response =
            await fetch("/chat", {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            });

        const data =
            await response.json();

        hideTyping();

        addBotMessage(
            data.answer,
            data.confidence,
            data.sentiment
        );

        lastBotResponse =
            data.answer;

        loadAnalytics();

    } catch (error) {

        hideTyping();

        addBotMessage(
            "Server error. Please try again.",
            0,
            "Neutral"
        );

        console.error(error);
    }
}

/* ==========================================================
   MESSAGE BUILDERS
========================================================== */

function addUserMessage(message) {

    const html = `

    <div class="user-message">

        <div class="message-content">

            <p>${message}</p>

        </div>

        <div class="message-avatar">

            <i class="fa-solid fa-user"></i>

        </div>

    </div>

    `;

    chatBox.insertAdjacentHTML(
        "beforeend",
        html
    );

    scrollChatToBottom();
}

function addBotMessage(
    message,
    confidence,
    sentiment
) {

    const html = `

    <div class="bot-message">

        <div class="message-avatar">

            <i class="fa-solid fa-robot"></i>

        </div>

        <div class="message-content">

            <p>${message}</p>

            <div class="message-meta">

                Confidence:
                ${confidence}% |

                Sentiment:
                ${sentiment}

            </div>

        </div>

    </div>

    `;

    chatBox.insertAdjacentHTML(
        "beforeend",
        html
    );

    scrollChatToBottom();
}

function scrollChatToBottom() {

    chatBox.scrollTop =
        chatBox.scrollHeight;
}

/* ==========================================================
   TYPING INDICATOR
========================================================== */

function showTyping() {

    if (typingIndicator) {

        typingIndicator.style.display =
            "flex";
    }
}

function hideTyping() {

    if (typingIndicator) {

        typingIndicator.style.display =
            "none";
    }
}

/* ==========================================================
   THEME TOGGLE
========================================================== */

function initializeTheme() {

    const savedTheme =
        localStorage.getItem("theme");

    if (savedTheme === "dark") {

        document.body.classList.add(
            "dark-mode"
        );
    }

    if (themeToggle) {

        themeToggle.addEventListener(
            "click",
            () => {

                document.body.classList.toggle(
                    "dark-mode"
                );

                const currentTheme =
                    document.body.classList.contains(
                        "dark-mode"
                    )
                        ? "dark"
                        : "light";

                localStorage.setItem(
                    "theme",
                    currentTheme
                );

                showToast(
                    `Theme changed to ${currentTheme}`
                );
            }
        );
    }
}

/* ==========================================================
   ANALYTICS
========================================================== */

async function loadAnalytics() {

    try {

        const response =
            await fetch("/analytics");

        const data =
            await response.json();

        updateAnalytics(data);

    } catch (error) {

        console.error(
            "Analytics Error:",
            error
        );
    }
}

function updateAnalytics(data) {

    const totalChats =
        document.getElementById(
            "totalChats"
        );

    const avgConfidence =
        document.getElementById(
            "avgConfidence"
        );

    const positiveCount =
        document.getElementById(
            "positiveCount"
        );

    const neutralCount =
        document.getElementById(
            "neutralCount"
        );

    const negativeCount =
        document.getElementById(
            "negativeCount"
        );

    if (totalChats) {

        totalChats.innerText =
            data.total_conversations || 0;
    }

    if (avgConfidence) {

        avgConfidence.innerText =
            `${data.average_confidence || 0}%`;
    }

    if (positiveCount) {

        positiveCount.innerText =
            data.sentiment_stats.Positive || 0;
    }

    if (neutralCount) {

        neutralCount.innerText =
            data.sentiment_stats.Neutral || 0;
    }

    if (negativeCount) {

        negativeCount.innerText =
            data.sentiment_stats.Negative || 0;
    }

    const topQuestions =
        document.getElementById(
            "topQuestions"
        );

    if (
        topQuestions &&
        data.most_asked_questions
    ) {

        topQuestions.innerHTML = "";

        Object.entries(
            data.most_asked_questions
        ).forEach(
            ([question, count]) => {

                topQuestions.innerHTML += `

                <li>

                    ${question}
                    (${count})

                </li>

                `;
            }
        );
    }
}

/* ==========================================================
   VOICE RECOGNITION
========================================================== */

function initializeVoiceRecognition() {

    if (
        !("webkitSpeechRecognition" in window)
    ) {

        return;
    }

    const recognition =
        new webkitSpeechRecognition();

    recognition.continuous = false;

    recognition.interimResults = false;

    recognition.lang = "en-US";

    if (voiceBtn) {

        voiceBtn.addEventListener(
            "click",
            () => {

                recognition.start();

                showToast(
                    "Listening..."
                );
            }
        );
    }

    recognition.onresult = function (
        event
    ) {

        const transcript =
            event.results[0][0]
                .transcript;

        userInput.value =
            transcript;

        sendMessage();
    };
}

/* ==========================================================
   TEXT TO SPEECH
========================================================== */

if (speakBtn) {

    speakBtn.addEventListener(
        "click",
        () => {

            if (
                !lastBotResponse
            ) {

                showToast(
                    "No response available."
                );

                return;
            }

            const utterance =
                new SpeechSynthesisUtterance(
                    lastBotResponse
                );

            speechSynthesis.speak(
                utterance
            );
        }
    );
}

/* ==========================================================
   EXPORT CHAT
========================================================== */

function initializeExport() {

    if (!exportBtn) {

        return;
    }

    exportBtn.addEventListener(
        "click",
        () => {

            const text =
                chatBox.innerText;

            const blob =
                new Blob(
                    [text],
                    {
                        type:
                            "text/plain"
                    }
                );

            const url =
                URL.createObjectURL(
                    blob
                );

            const link =
                document.createElement(
                    "a"
                );

            link.href = url;

            link.download =
                "pinguaai_chat.txt";

            link.click();

            URL.revokeObjectURL(
                url
            );

            showToast(
                "Chat exported."
            );
        }
    );
}

/* ==========================================================
   CLEAR CHAT
========================================================== */

function initializeClearChat() {

    if (!clearChatBtn) {

        return;
    }

    clearChatBtn.addEventListener(
        "click",
        () => {

            chatBox.innerHTML = "";

            addBotMessage(
                "Chat cleared successfully.",
                100,
                "Neutral"
            );

            showToast(
                "Chat cleared."
            );
        }
    );
}

/* ==========================================================
   TOAST
========================================================== */

function showToast(message) {

    const toast =
        document.getElementById(
            "toast"
        );

    if (!toast) {

        return;
    }

    toast.innerText =
        message;

    toast.classList.add(
        "show"
    );

    setTimeout(() => {

        toast.classList.remove(
            "show"
        );

    }, 3000);
}

