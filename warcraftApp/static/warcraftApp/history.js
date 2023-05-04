
function swapHistory(expansion) {
    console.log("here");

    var head = document.getElementById("h-" + expansion);
    var expac = document.getElementById("expac-" + expansion);
    var desc = document.getElementById("desc-" + expansion);

    if (head.style.display === "block") {
        head.style.display = "none";
        expac.style.display = "none";
        desc.style.display = "block";
    } else {
        head.style.display = "block";
        expac.style.display = "block";
        desc.style.display = "none";
    }

};

