const promptInput = document.getElementById("prompt");
const charCount = document.getElementById("charCount");
const routeButton = document.getElementById("routeButton");
const buttonText = document.getElementById("buttonText");

const resultCard = document.getElementById("resultCard");
const intentElement = document.getElementById("intent");
const confidenceElement = document.getElementById("confidence");
const confidenceBar = document.getElementById("confidenceBar");
const responseElement = document.getElementById("response");

const errorMessage = document.getElementById("errorMessage");
const copyButton = document.getElementById("copyButton");


// Character counter
promptInput.addEventListener("input", () => {
    charCount.textContent = promptInput.value.length;
});


// Example prompt buttons
document.querySelectorAll(".example-prompts button").forEach(button => {

    button.addEventListener("click", () => {

        promptInput.value = button.dataset.prompt;

        charCount.textContent = promptInput.value.length;

        promptInput.focus();

    });

});


// Show error
function showError(message) {

    errorMessage.textContent = message;

    errorMessage.style.display = "block";
}


// Hide error
function hideError() {

    errorMessage.style.display = "none";

}


// Loading state
function setLoading(loading) {

    if (loading) {

        routeButton.disabled = true;

        routeButton.classList.add("loading");

        buttonText.textContent = "Routing...";

    } else {

        routeButton.disabled = false;

        routeButton.classList.remove("loading");

        buttonText.textContent = "Route Prompt";

    }

}


// Route prompt
async function routePrompt() {

    hideError();

    const message = promptInput.value.trim();

    if (!message) {

        showError("Please enter a prompt before routing.");

        promptInput.focus();

        return;

    }


    setLoading(true);

    resultCard.classList.add("hidden");


    try {

        const response = await fetch("/api", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.error || "Something went wrong while processing the prompt."
            );

        }


        // Intent
        intentElement.textContent = data.intent || "Unknown";


        // Confidence
        const confidence = Number(data.confidence) || 0;

        const percentage = confidence <= 1
            ? confidence * 100
            : confidence;

        confidenceElement.textContent =
            `${percentage.toFixed(1)}%`;

        confidenceBar.style.width =
            `${Math.min(percentage, 100)}%`;


        // Response
        responseElement.textContent =
            data.response || "No response returned.";


        // Show result
        resultCard.classList.remove("hidden");


        // Scroll to result
        setTimeout(() => {

            resultCard.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });

        }, 100);


    } catch (error) {

        console.error(error);

        showError(
            error.message ||
            "Unable to connect to the prompt router."
        );

    } finally {

        setLoading(false);

    }

}


// Route button
routeButton.addEventListener("click", routePrompt);


// Allow Ctrl + Enter / Cmd + Enter
promptInput.addEventListener("keydown", event => {

    if (
        event.key === "Enter" &&
        (event.ctrlKey || event.metaKey)
    ) {

        routePrompt();

    }

});


// Copy response
copyButton.addEventListener("click", async () => {

    const response = responseElement.textContent;

    if (!response || response === "—") {
        return;
    }

    try {

        await navigator.clipboard.writeText(response);

        copyButton.textContent = "Copied!";

        setTimeout(() => {
            copyButton.textContent = "Copy";
        }, 1500);

    } catch (error) {

        console.error("Copy failed:", error);

    }

});