document.addEventListener("DOMContentLoaded", function () {
    const inputList = document.getElementById("inputList");
    const inputList2 = document.getElementById("inputList2");
    const axial1942in = document.getElementById("axial1942in");
    const axial1942out = document.getElementById("axial1942out");
    const zoneRow1965In = document.getElementById("zonerow1965in");
    const zoneRow1965Out = document.getElementById("zonerow1965out");
    const axial2000in = document.getElementById("axial2000in");
    const axial2000out = document.getElementById("axial2000out");
    const formatBLin = document.getElementById("formatblin");
    const formatBLout = document.getElementById("formatblout");

    // Funkcja do aktualizacji listy wyjścia w zależności od wybranej opcji wejścia
    function updateOutputList() {
        const selectedInput = inputList.value;
    
        // Usuwamy wszystkie opcje z listy wyjścia
        inputList2.innerHTML = "";
    
        // Kopiujemy opcje z listy wejścia do listy wyjścia i usuwamy opcję wybraną na liście wejścia
        for (const option of inputList.options) {
            if (option.value !== selectedInput || option.value === "empty") {
                const clonedOption = option.cloneNode(true);
                inputList2.appendChild(clonedOption);
            }
        }
    
        // Pokazujemy lub ukrywamy odpowiednie kontenery w zależności od wybranej opcji wejścia
        if (selectedInput === "opcja1") {
            zoneRow1965In.style.display = "none";
            axial1942in.style.display = "flex";
            axial2000in.style.display = "none";
            formatBLin.style.display = "none";
        } else if (selectedInput === "opcja2") {
            zoneRow1965In.style.display = "flex";
            axial1942in.style.display = "none";
            axial2000in.style.display = "none";
            formatBLin.style.display = "none";
        } else if (selectedInput === "opcja3") {
            zoneRow1965In.style.display = "none";
            axial1942in.style.display = "none";
            axial2000in.style.display = "none";
            formatBLin.style.display = "none";
        } else if (selectedInput === "opcja4") {
            zoneRow1965In.style.display = "none";
            axial1942in.style.display = "none";
            axial2000in.style.display = "flex";
            formatBLin.style.display = "none";
        } else if (selectedInput === "opcja5") {
            zoneRow1965In.style.display = "none";
            axial1942in.style.display = "none";
            axial2000in.style.display = "none";
            formatBLin.style.display = "flex";
        } else if (selectedInput === "opcja6") {
            zoneRow1965In.style.display = "none";
            axial1942in.style.display = "none";
            axial2000in.style.display = "none";
            formatBLin.style.display = "flex";
        } else {
            zoneRow1965In.style.display = "none";
            axial1942in.style.display = "none";
            axial2000in.style.display = "none";
            formatBLin.style.display = "none";
        }
    }    
    

    // Wywołujemy funkcję aktualizującą listę wyjścia na start
    updateOutputList();

    // Nasłuchujemy zmiany opcji wejścia
    inputList.addEventListener("change", updateOutputList);

    // Nasłuchujemy zmiany opcji wyjścia
    inputList2.addEventListener("change", function () {
        const selectedInput2 = inputList2.value;

        // Sprawdzamy, czy wybrano "empty", jeśli tak, ukrywamy wszystkie kontenery wyjścia
        if (selectedInput2 === "empty") {
            axial1942out.style.display = "none";
            zoneRow1965Out.style.display = "none";
            axial2000out.style.display = "none";
            formatBLout.style.display = "none";
        } else {
            // W przeciwnym przypadku, ukrywamy wszystkie kontenery wyjścia
            // i pokazujemy tylko odpowiedni kontener na podstawie wybranej opcji
            axial1942out.style.display = "none";
            zoneRow1965Out.style.display = "none";
            axial2000out.style.display = "none";
            formatBLout.style.display = "none";

            // Pokazujemy odpowiedni kontener wyjścia w zależności od wybranej opcji wyjścia
            if (selectedInput2 === "opcja1") {
                axial1942out.style.display = "flex";
            } else if (selectedInput2 === "opcja2") {
                zoneRow1965Out.style.display = "flex";
            } else if (selectedInput2 === "opcja4") {
                axial2000out.style.display = "flex";
            } else if (selectedInput2 === "opcja5" || selectedInput2 === "opcja6") {
                formatBLout.style.display = "flex";
            }
        }
    });
});