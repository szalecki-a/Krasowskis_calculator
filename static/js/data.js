document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementById("submitButton");

    submitButton.addEventListener('click', function () {
        const inputCoordinateFormat = document.getElementById("inputList").value;
        const outputCoordinateFormat = document.getElementById("inputList2").value;
        const dataEntered = document.getElementById("inputText").value;

        const containers = ["axial1942in", "axial1942out", "zonerow1965in", "zonerow1965out", "axial2000in", "axial2000out", "formatblin", "formatblout"];
    
        const inputData = {
            inputCoordinateFormat,
            outputCoordinateFormat,
            dataEntered
        };

        
        containers.forEach(containerId => {
            inputData[containerId] = getValueFromGroup(containerId);
        });



        fetch('http://127.0.0.1:5000/main', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputData: inputData }),
        })
        .then(response => response.json())
        .then(data => {
            // Obsłuż odpowiedź od backendu
            console.log(data);

            const outputContainer = document.getElementById("outputContainer");
            const formatbloutValue = getValueFromGroup("formatblout");

            if (data.hasOwnProperty('message')) {
                outputContainer.textContent = data.message;
            } else {
                let formattedData = "";
                if (Array.isArray(data)) {
                    if (formatbloutValue === '1') {
                        formattedData = data.map(item => item.join(', ')).join('\n');
                    } else if (formatbloutValue === '2') {
                        formattedData = data.map(item => {
                            const modifiedItem = item.replace(/\./g, "'");
                            const finalItem = modifiedItem.replace(/'\\'/g, "'");
                            return finalItem;
                        }).join('\n');
                    }
                } else {
                    formattedData = JSON.stringify(data);
                }

                outputContainer.value = formattedData;
            }
        })
        .catch(error => {
            // Obsłuż błąd
            console.error('Błąd:', error);
        });

    });

    function getValueFromGroup(groupId) {
        const radioButtons = document.querySelectorAll(`#${groupId} input[type="radio"]`);

        let selectedValue = null;

        radioButtons.forEach(radioButton => {
            if (radioButton.checked) {
                selectedValue = radioButton.value;
            }
        });

        return selectedValue;
    }
});