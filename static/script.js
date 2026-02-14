gsap.from(".glass-card", {duration:1, y:50, opacity:0});
gsap.from(".title", {duration:1, y:-30, opacity:0});

document.getElementById("timingForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    const resultDiv = document.getElementById("result");
    resultDiv.classList.remove("hidden");
    resultDiv.innerHTML = "Analyzing...";

    const response = await fetch("/evaluate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    let color = "#4CAF50";
    if (result.decision === "WAIT") color = "#ff5252";
    if (result.decision === "CAUTION") color = "#ff9800";

    resultDiv.innerHTML = `
        <h2 style="color:${color}">${result.decision}</h2>
        <h4>${result.opportunity_window}</h4>
        <p id="typing"></p>
    `;

    let text = result.explanation;
    let i = 0;
    const typing = document.getElementById("typing");

    function typeEffect() {
        if (i < text.length) {
            typing.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeEffect, 15);
        }
    }
    typing.innerHTML = "";
    typeEffect();
});
