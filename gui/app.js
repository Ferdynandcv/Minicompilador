//elements
let playButton = document.getElementById("play");
let input = document.getElementById("input");
let simbols = document.getElementById("simbols");
let errors = document.getElementById("errors");
let playImage = document.getElementById("playImage");

//functions

eel.expose(showGif)
function showGif(type){
	playImage.src =  type === "error" ? "./assets/errors.gif" : "./assets/noErrors.gif";
	setTimeout(()=>{
	  playImage.src = "./assets/play.png"
  },2000)

}

eel.expose(printGui)
function printGui(text,type){
	if(type === "errors"){
		errors.value = text;
	}
	else{
		simbols.value = text;
	}
}

function cleanResults(){
	simbols.value = "";
	errors.value = "";
	eel.clean()
}

(function events(){
	document.addEventListener('DOMContentLoaded', () =>{
	});

	playButton.addEventListener("click", () =>{
		let code = input.value;
		code != "" && eel.analizar(code);
		cleanResults();
	});

	input.addEventListener("keyup", ()=>{
		cleanResults();
	})

})();

