const nextStepButton = document.getElementById('submit');
const backStepButton = document.getElementById('back-step');
const container = document.getElementById('container');

nextStepButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

backStepButton.addEventListener('click', () => {
	let recList = document.getElementById("recList");
	recList.innerHTML = "";
	container.classList.remove("right-panel-active");
});

function submitData() {
	let nin = document.getElementById('n')
	let poh = document.getElementById('p')
	let pot = document.getElementById('k')
	let tem = document.getElementById('temp')
	let hum = document.getElementById('humidity')
	let PH = document.getElementById('ph')
	let rains = document.getElementById('rain')

	console.log()

	jsonObject = {
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

	axios.get('http://127.0.0.1:8000/api/advtop5', config).then(function (response) {
		let recList = document.getElementById("recList");
		let preds = response.data.predictions

		for(let pred of preds) {
			recList.innerHTML += "<li>" + pred + "</li>";
		}
		console.log(response.data.predictions);
	})


}