document.addEventListener("DOMContentLoaded", function () {
    const inputText = document.getElementById("inputText");
    const errorMessage = document.getElementById("errorMessage");
    const submitButton = document.getElementById("submitButton");
    let BLinValue = "1";
    let hasError = false; // flaga dla przycisku

    function checkPattern() {
        const inputValue = inputText.value;
        let pattern;
        
        if (BLinValue === '2') {
            pattern = /[^NnSsWwEe0-9 ,.;'"°\s\r\n]+/;
        } else {
            pattern = /[^0-9 ,.;\s\r\n]+/;
        }
        
        if (pattern.test(inputValue)) {
            inputText.style.borderColor = "red";
            errorMessage.style.display = "flex";
            errorMessage.textContent = "Tekst zawiera niedozwolone znaki.";
            hasError = true; 
        } else {
            errorMessage.style.display = "none";
            inputText.style.borderColor = "";
            hasError = false; // zmiana flagi na false aby uniemożliwić wysłanie protokołu
        }
    }

    const radioButtons = document.querySelectorAll('#formatblin input[type="radio"]');
    radioButtons.forEach(radioButton => {
        radioButton.addEventListener("change", function () {
            BLinValue = radioButton.value;

            checkPattern();
            updateSubmitButton(); // update przycisku "Wyślij" po zmianie przycisku radio
        });
    });

    checkPattern();

    inputText.addEventListener("input", function () {
        checkPattern();
        updateSubmitButton(); // update przycisku "Wyślij" po zmianie przycisku radio
    });

    function updateSubmitButton() {
        if (hasError) {
            submitButton.disabled = true; // wyłączenie przycisku w przypadku pojawienia się błedu pattern
        } else {
            submitButton.disabled = false; // włączenie przycisku w przypadku braku błedu pattern
        }
    }
});
