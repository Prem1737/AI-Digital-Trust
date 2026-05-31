async function predict() {

    const transparency = document.getElementById("transparency").value;
    const fairness = document.getElementById("fairness").value;
    const privacy = document.getElementById("privacy").value;
    const security = document.getElementById("security").value;
    const explainability = document.getElementById("explainability").value;

    const response = await fetch(
        `http://127.0.0.1:5000/predict?transparency=${transparency}&fairness=${fairness}&privacy=${privacy}&security=${security}&explainability=${explainability}`
    );

    const data = await response.json();

    let level = "";

    if (data.trust_score >= 80) {
        level = " HIGH TRUST";
    } else if (data.trust_score >= 50) {
        level = " MEDIUM TRUST";
    } else {
        level = " LOW TRUST";
    }

    document.getElementById("result").innerHTML =
        "Trust Score: " + data.trust_score +
        "<br><br>" + level;
}
