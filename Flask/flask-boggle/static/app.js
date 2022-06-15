const $guessForm = $('#guessForm')
const $guessInput = $('#guessInput')
const $responseText = $('#response')
const $scoreDisplay = $('#score')
const $timerDisplay = $('#timer')
const $hiscoreDisplay = $('#hi-score')
const $gamesPlayedDisplay = $('#gamesPlayed')

class BoggleGame {

    constructor(seconds){
        this.score = 0
        this.seconds = seconds
        this.guesses = new Set()
    }

    // submits http request to server with the form info
    async submitGuess(event){
        event.preventDefault();
    
        //stops any furthur guess once the timer reaches 0
        if(this.seconds <= 0){
            return
        }
    
        const guess = $guessInput.val();

        console.log(this)        
        const response = await this.getResponse(guess);
        console.log(response)
        this.updatePage(response);
        this.updateScore(response,guess);
    
        //empty the input field
        $guessForm.trigger('reset');
    
    }
    
    async getResponse(word){
        return await axios.post('/',{guess:word});
    }
    
    
    updatePage(response){
        $responseText.text(response.data.result);
    }
    
    //Update the score if the guess is not already been guessed and it is a word/on the board
    updateScore(response,guess){
        if(response.data.result === 'ok' && !this.guesses.has(guess)){
            this.guesses.add(guess);
            this.score += guess.length;
            $scoreDisplay.text(this.score);
        }
    }
    
    startTimer(){
    
        setInterval(()=>{
            //once timer reaches 0, stop the timer and send the score to the server
            if(this.seconds <= 0) {
                clearInterval(1);
                this.endGame();
                return
            }
    
            this.seconds--;
            $timerDisplay.text(this.seconds)
    
        },1000);
    }
    
    //sends the score to the server, increments games played, updates high score
    async endGame(){
        const response = await axios.post('/endgame',{'score':this.score})
        const highscore = response.data.highscore
        const gamesPlayed = response.data.games_played
        $hiscoreDisplay.text(highscore)
        $gamesPlayedDisplay.text(gamesPlayed)
    }
    
}

//initialize a new game
const newGame = new BoggleGame(60)

//start timer on pageload
$(newGame.startTimer())

//clickevent handler for the submit button
$guessForm.on('submit',newGame.submitGuess.bind(newGame));