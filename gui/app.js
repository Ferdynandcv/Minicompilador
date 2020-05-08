//elements
let playButton = document.getElementById("play");
let input = document.getElementById("input");
let simbols = document.getElementById("simbols");
let errors = document.getElementById("errors");
let playImage = document.getElementById("playImage");


//functions

function launchGif(type){
	playImage.src =  type === "error" ? "./assets/errors.gif" : "./assets/noErrors.gif";
	setTimeout(()=>{
	  playImage.src = "./assets/play.png"
  },2000)

}

function cleanResults(){
	simbols.value = "";
	errors.value = "";
}

(function events(){
	document.addEventListener('DOMContentLoaded', () =>{
		launchGif("slfjaerror")
	});

	playButton.addEventListener("click", () =>{
		let code = input.value;
		code != "" && console.log(code);
	});

	input.addEventListener("keyup", ()=>{
		cleanResults();
	})


})();

