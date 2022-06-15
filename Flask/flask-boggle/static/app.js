const $guessForm = $('#guessForm')
const $guessInput = $('#guessInput')
const $responseText = $('#response')

// submits http request to server with the form info
async function submitGuess(event){
    event.preventDefault();
    const guess = $guessInput.val();

    response = await getResponse(guess);
    updatePage(response);

}

async function getResponse(word){
    return await axios.post('/',{guess:word});
}

function updatePage(response){
    $responseText.text(response.data.result);
}

//clickeven handler for the submit button
$guessForm.on('submit',submitGuess);