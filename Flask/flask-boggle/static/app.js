const $guessForm = $('#guessForm')
const $guessInput = $('#guessInput')
const $responseText = $('#response')
const $scoreDisplay = $('#score')
const $timerDisplay = $('#timer')

let score = 0
let seconds=60
const guesses = new Set()

$(startTimer())

// submits http request to server with the form info
async function submitGuess(event){
    event.preventDefault();

    //stops any furthur guess once the timer reaches 0
    if(seconds <= 0){
        return
    }

    const guess = $guessInput.val();

    response = await getResponse(guess);
    updatePage(response);
    updateScore(response,guess);

    //empty the input field
    $guessForm.trigger('reset');

}

async function getResponse(word){
    return await axios.post('/',{guess:word});
}


function updatePage(response){
    $responseText.text(response.data.result);
}

//Update the score if the guess is not already been guessed and it is a word/on the board
function updateScore(response,guess){
    if(response.data.result === 'ok' && !guesses.has(guess)){
        guesses.add(guess);
        score += guess.length;
        $scoreDisplay.text(score);
    }
}

function startTimer(){

    setInterval(()=>{

        if(seconds <= 0) {
            clearInterval(1);
            return
        }

        seconds--;
        $timerDisplay.text(seconds)

    },1000);
}

//clickevent handler for the submit button
$guessForm.on('submit',submitGuess);