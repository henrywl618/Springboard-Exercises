/** Connect Four
 *
 * Player 1 and 2 alternate turns. On each turn, a piece is dropped down a
 * column until a player gets four-in-a-row (horiz, vert, or diag) or until
 * board fills (tie)
 */



class Game{

  constructor(width,height){
    this.WIDTH = width;
    this.HEIGHT = height;
    this.players = [];
    this.currPlayer = this.players[0]; // active player: 1 or 2
    this.board = []; // array of rows, each row is array of cells  (board[y][x])
    this.gameFinished = false;
  }

// * makeBoard: create in-JS board structure:
//  *   board = array of rows, each row is array of cells  (board[y][x])
 

  makeBoard() {
    for (let y = 0; y < this.HEIGHT; y++) {
      this.board.push(Array.from({ length: this.WIDTH }));
    }
  }

  /** makeHtmlBoard: make HTML table and row of column tops. */

  makeHtmlBoard() {
    const board = document.getElementById('board');
    const startBtn = document.querySelector("#startBtn");
  
    // make column tops (clickable area for adding a piece to that column)
    const top = document.createElement('tr');
    top.setAttribute('id', 'column-top');
    top.addEventListener('click', this.handleClick.bind(this));
    startBtn.addEventListener('click', this.initGame.bind(this));
  
    for (let x = 0; x < this.WIDTH; x++) {
      const headCell = document.createElement('td');
      headCell.setAttribute('id', x);
      //create the pieces that will show in the top row when we hover over it
      const newPiece = document.createElement('div');
      newPiece.classList.add(`piece`,'hidden');
      headCell.append(newPiece);
      this.addHoverEffect(headCell);
      top.append(headCell)
    }
  
    board.append(top);
  
    // make main part of board
    for (let y = 0; y < this.HEIGHT; y++) {
      const row = document.createElement('tr');
  
      for (let x = 0; x < this.WIDTH; x++) {
        const cell = document.createElement('td');
        cell.setAttribute('id', `${y}-${x}`);
        row.append(cell);
      }
  
      board.append(row);
    }
  }

  /** findSpotForCol: given column x, return top empty y (null if filled) */

  findSpotForCol(x) {
    for (let y = this.HEIGHT - 1; y >= 0; y--) {
      if (!this.board[y][x]) {
        return y;
      }
    }
    return null;
  }
  /** placeInTable: update DOM to place piece into HTML table of board */

  placeInTable(y, x) {
    const piece = document.createElement('div');
    piece.classList.add('piece');
    piece.style.backgroundColor = `${this.currPlayer.color}`
    piece.style.top = -50 * (y + 2);

    const spot = document.getElementById(`${y}-${x}`);
    spot.append(piece);
  }

  /** endGame: announce game end */

  endGame(msg) {
    alert(msg);
  }

  /** handleClick: handle click of column top to play piece */

  handleClick(evt) {
    //show alert if the game hasnt started
    if(this.board.length === 0){
      alert('Please start the game');
      return;
    }

    if(this.gameFinished) return; //if the current game is finished do nothing

    // get x from ID of clicked cell
    const x = +evt.target.id;

    // get next spot in column (if none, ignore click)
    const y = this.findSpotForCol(x);
    if (y === null) {
      return;
    }

    // place piece in board and add to HTML table
    this.board[y][x] = this.currPlayer.id;
    this.placeInTable(y, x);
    
    // check for win
    if (this.checkForWin()) {
      this.gameFinished = true;
      return this.endGame(`Player ${this.currPlayer.id} won!`);
    }
    
    // check for tie
    if (this.board.every(row => row.every(cell => cell))) {
      this.gameFinished = true;
      return this.endGame('Tie!');
    }
      
    // switch players
    this.currPlayer = this.currPlayer === this.players[0] ? this.players[1] : this.players[0];

    //change color of the top piece to the current players color
    evt.target.querySelector('div').style.backgroundColor = this.currPlayer.color;
  }

  /** checkForWin: check board cell-by-cell for "does a win start here?" */

  checkForWin() {
    function _win(cells) {
      // Check four cells to see if they're all color of current player
      //  - cells: list of four (y, x) cells
      //  - returns true if all are legal coordinates & all match currPlayer
      return cells.every(
        ([y, x]) =>
          y >= 0 &&
          y < this.HEIGHT &&
          x >= 0 &&
          x < this.WIDTH &&
          this.board[y][x] === this.currPlayer.id
      );
    }

    const __win = _win.bind(this); //Bind the game object to the function

    for (let y = 0; y < this.HEIGHT; y++) {
      for (let x = 0; x < this.WIDTH; x++) {
        // get "check list" of 4 cells (starting here) for each of the different
        // ways to win
        const horiz = [[y, x], [y, x + 1], [y, x + 2], [y, x + 3]];
        const vert = [[y, x], [y + 1, x], [y + 2, x], [y + 3, x]];
        const diagDR = [[y, x], [y + 1, x + 1], [y + 2, x + 2], [y + 3, x + 3]];
        const diagDL = [[y, x], [y + 1, x - 1], [y + 2, x - 2], [y + 3, x - 3]];

        // find winner (only checking each win-possibility as needed)
        if (__win(horiz)|| __win(vert) || __win(diagDR) || __win(diagDL)) {
          console.log(true);
          return true;
        }
      }
    }
  }

  addHoverEffect(td){

    td.addEventListener("mouseover", (evt) => {
      console.log(evt.target);
      evt.target.querySelector('div').style.backgroundColor = this.currPlayer.color;
      evt.target.querySelector('div').classList.toggle('hidden');
      console.log(evt.target);
    })
    td.addEventListener("mouseout", (evt) => {
      console.log(evt.target);
      evt.target.querySelector('div').classList.toggle('hidden');
  
    })

  }

  initGame(evt){
    evt.preventDefault();
    document.querySelector('#board').innerHTML = '';
    this.board = [];
    const Player1 = new Player(1, document.querySelector('#P1Color').value);
    const Player2 = new Player(2, document.querySelector('#P2Color').value);
    this.players = [Player1,Player2];
    this.currPlayer = Player1;
    this.gameFinished = false;
    currentGame.makeBoard();
    currentGame.makeHtmlBoard();
  };

};


class Player{
  constructor(id,color){
    this.id = id;
    this.color = color;
  }
};



const currentGame = new Game(7,6);
currentGame.makeHtmlBoard();



