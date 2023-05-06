//Name: Maggie Herms
//File: history.js
//Last edit: 5/5/2023
//Function to swap timeline content from name and date to description

function swapHistory(expansion) {

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

