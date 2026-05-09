// SPEECH RECOGNITION
const downloadBtn =
    document.getElementById(
        "downloadBtn"
    );
const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

const recognition =
    new SpeechRecognition();

recognition.lang = "en-US";

recognition.continuous = false;

recognition.interimResults = false;
const graphBtn =
document.getElementById(
    "graphBtn"
);

const graphContainer =
document.getElementById(
    "graphContainer"
);
const analyzeBtn =
    document.getElementById("analyzeBtn");
    const micBtn =
    document.getElementById("micBtn");

const textInput =
    document.getElementById("textInput");


// ANALYZE BUTTON
analyzeBtn.addEventListener(
    "click",
    async () => {

        const text =
            textInput.value.trim();

        // EMPTY CHECK
        if(text === ""){

            alert(
                "Please enter text"
            );

            return;
        }
        document.getElementById(
    "loadingText"
).style.display = "block";

        try{

            const response =
                await fetch(
                    "http://127.0.0.1:8000/analyze",
                    {
                        method:"POST",

                        headers:{
                            "Content-Type":
                            "application/json"
                        },

                        body:JSON.stringify({
                            text:text
                        })
                    }
                );

            const data =
                await response.json();
                document.getElementById(
    "loadingText"
).style.display = "none";

            console.log(data);
            // GRAPH
const ctx =
    document
    .getElementById(
        "analyticsChart"
    );


// REMOVE OLD GRAPH
if(window.myChart){

    window.myChart.destroy();

}


// CREATE NEW GRAPH
window.myChart =
new Chart(ctx, {

    type: "bar",

    data: {

        labels: [

            "Confidence",

            "Communication",

            "Hesitation"

        ],

        datasets: [{

            label:
            "AI Communication Scores",

            data: [

                data.confidence_score,

                data.communication_score,

                data.hesitation_score

            ],

            borderWidth: 1

        }]

    },

    options: {

        responsive: true,
        maintainAspectRatio: false,

        scales: {

            y: {

                beginAtZero: true,

                max: 100

            }

        }

    }

});

            // UPDATE UI
            document.getElementById(
                "confidenceScore"
            ).innerHTML =
                data.confidence;

            document.getElementById(
                "emotionScore"
            ).innerHTML =
                data.emotion;

            document.getElementById(
                "communicationScore"
            ).innerHTML =
                data.communication;

            document.getElementById(
                "hesitationScore"
            ).innerHTML =
                data.hesitation;
                // SUGGESTIONS
const suggestionsList =
document.getElementById(
    "suggestionsList"
);

suggestionsList.innerHTML = "";

data.suggestions.forEach(
    (suggestion) => {

        suggestionsList.innerHTML += `

        <li>

            ${suggestion}

        </li>

        `;

    }
);

        }

        catch(error){
            document.getElementById(
    "loadingText"
).style.display = "none";

            console.log(error);

            alert(
                "Backend Connection Failed"
            );

        }

    }
);
// GRAPH BUTTON
graphBtn.addEventListener(
    "click",
    () => {

        if(
            graphContainer.style.display
            === "block"
        ){

            graphContainer.style.display =
            "none";

            graphBtn.innerHTML =
            "Show Analytics Graph";

        }

        else{

            graphContainer.style.display =
            "block";

            graphBtn.innerHTML =
            "Hide Analytics Graph";

        }

    }
);
// MICROPHONE BUTTON
micBtn.addEventListener(
    "click",
    () => {

        recognition.start();

    }
);


// SPEECH RESULT
recognition.onresult = (event) => {

    const transcript =
        event.results[0][0].transcript;

    textInput.value =
        transcript;

};


// ERROR
// recognition.onerror = (event) => {

//     alert(
//         "Speech recognition error"
//     );

//     console.log(event.error);

// };
recognition.onerror = (event) => {

    console.log(event.error);

    alert(event.error);

};
// DOWNLOAD PDF REPORT
downloadBtn.addEventListener(
    "click",
    () => {

        window.print();

    }
);