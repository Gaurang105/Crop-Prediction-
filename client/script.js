const nextStepButton = document.getElementById('next-step');
const backStepButton = document.getElementById('back-step');
const container = document.getElementById('container');

nextStepButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

backStepButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});