function calculateTrust(){

    let score = Math.floor(Math.random() * 100) + 1;

    document.getElementById("result").innerHTML =
    "Trust Score: " + score + "%";
}
