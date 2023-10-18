function handleInformatorIcon1() {
    const informator1 = document.getElementById('informator1');
    const tooltip1 = document.getElementById('tooltip1');
    
    // Nasłuchujemy najechania kursorem na ikonkę informator1
    informator1.addEventListener('mouseenter', function () { 
        const selectedInput = document.getElementById('inputList').value;
        let tooltip1Text  = '';

        // Ustawienie tekstu w zależności od wybranej pozycji
        switch (selectedInput) {
            case 'empty':
                tooltip1Text = 'Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego';
                break;
            case 'opcja1':
                tooltip1Text = 'Tekst dla opcji 1';
                break;
            case 'opcja2':
                tooltip1Text = 'Tekst dla opcji 2';
                break;
            case 'opcja3':
                tooltip1Text = 'Tekst dla opcji 3';
                break;
            case 'opcja4':
                tooltip1Text = 'Tekst dla opcji 4';
                break;
            case 'opcja5':
                tooltip1Text = 'Tekst dla opcji 5';
                break;
            case 'opcja6':
                tooltip1Text = 'Tekst dla opcji 6';
                break;
            default:
                tooltip1Text = 'Domyślny tekst';
                break;
        }
        tooltip1.textContent = tooltip1Text;
        tooltip1.style.display = 'inline-block'
    });

    // Obsługa opuszczenia kursora z ikonki informator1
    informator1.addEventListener('mouseleave', function () {
        tooltip1.style.display = 'none';
    });
}


function handleInformatorIcon2() {
    const informator2 = document.getElementById('informator2');
    const tooltip2 = document.getElementById('tooltip2');
    
    // Nasłuchujemy najechania kursorem na ikonkę informator2
    informator2.addEventListener('mouseenter', function () { 
        const selectedInput2 = document.getElementById('inputList2').value;
        let tooltip2Text  = '';

        // Ustawienie tekstu w zależności od wybranej pozycji
        switch (selectedInput2) {
            case 'empty':
                tooltip2Text = 'Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego Tekst dla pustego';
                break;
            case 'opcja1':
                tooltip2Text = 'Tekst dla opcji 1';
                break;
            case 'opcja2':
                tooltip2Text = 'Tekst dla opcji 2';
                break;
            case 'opcja3':
                tooltip2Text = 'Tekst dla opcji 3';
                break;
            case 'opcja4':
                tooltip2Text = 'Tekst dla opcji 4';
                break;
            case 'opcja5':
                tooltip2Text = 'Tekst dla opcji 5';
                break;
            case 'opcja6':
                tooltip2Text = 'Tekst dla opcji 6';
                break;
            default:
                tooltip2Text = 'Domyślny tekst';
                break;
        }
        tooltip2.textContent = tooltip2Text;
        tooltip2.style.display = 'inline-block'
    });

    // Obsługa opuszczenia kursora z ikonki informator2
    informator2.addEventListener('mouseleave', function () {
        tooltip2.style.display = 'none';
    });
}


function informationTextArea() {
    const textArea = document.getElementById('inputText');
    const inputList = document.getElementById('inputList');
    
    inputList.addEventListener('change', function () { 
        const selectedInput = inputList.value;

        // Ustawienie tekstu w zależności od wybranej pozycji
        if (selectedInput === "empty") {
            textArea.placeholder = 'Wybierz typ współrzędnych wejściowych';
        } else if (selectedInput === "opcja1") {
            textArea.placeholder = 'Tekst dla opcji 1';
        } else if (selectedInput === "opcja2") {
            textArea.placeholder = 'Tekst dla opcji 2';
        } else if (selectedInput === "opcja3") {
            textArea.placeholder = 'Tekst dla opcji 3';
        } else if (selectedInput === "opcja4") {
            textArea.placeholder = 'Tekst dla opcji 4';
        } else if (selectedInput === "opcja5") {
            textArea.placeholder = 'Tekst dla opcji 5';
        } else if (selectedInput === "opcja6") {
            textArea.placeholder = 'Tekst dla opcji 6';
        }
    });
}

// Wywołanie funkcji obsługującej ikonkę informator
handleInformatorIcon1();
handleInformatorIcon2();
informationTextArea();
