const nextStepButton = document.getElementById('submit');
const backStepButton = document.getElementById('back-step');
const container = document.getElementById('container');

nextStepButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

backStepButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

function submitData(){
	let nin = document.getElementById('n')
	let poh = document.getElementById('p')
	let pot = document.getElementById('k')
	let tem = document.getElementById('temp')
	let hum = document.getElementById('humidity')
	let PH = document.getElementById('ph')
	let rains = document.getElementById('rain')

	console.log()

	jsonObject={
		"N": nin.value,
		"P": poh.value,
		"K": pot.value,
		"temp": tem.value,
		"humidity": hum.value,
		"nature": "acidic",
		"rainfall": rains.value
	}
	let config = {
		params: jsonObject
	  }
	  
	  axios.get('http://127.0.0.1:8000/api/cropr', config).then(function(response) {
		  console.log(response);
	  })

}