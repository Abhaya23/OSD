var button = document.getElementById('b1');
var textParagraph = document.getElementById('textContent');
var textChanged = false;
button.addEventListener('click', function() {
    if (textChanged === false) {
        textParagraph.textContent = "First text";
        textChanged = true;
    } else {
        textParagraph.textContent = "Second text";
        textChanged = false;
    }
});