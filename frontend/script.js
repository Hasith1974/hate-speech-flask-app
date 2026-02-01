const prediction = document.getElementById("prediction");

function toggleDark() {
    document.body.classList.toggle("dark");
}

function detectHate() {
    const text = document.getElementById("inputText").value;
    if (!text.trim()) {
        alert("Please enter some text");
        return;
    }

    document.getElementById("loader").style.display = "block";
    document.getElementById("resultCard").style.display = "none";

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("loader").style.display = "none";
        document.getElementById("resultCard").style.display = "block";
        prediction.innerText = data.prediction;
    })
    .catch(() => alert("Server error"));
}
