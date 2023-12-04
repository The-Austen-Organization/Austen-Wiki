function evaluateMathExpression(expr) {
	const apiUrl = `https://api.mathjs.org/v4/?expr=${encodeURIComponent(expr)}`;

	return fetch(apiUrl)
		.then(response => {
			if (response.status >= 400) {
				return false;
			}
			return response.text();
		})
		.then(data => {
			return data;
	})
	.catch(error => {
		return false;
	});
}

evaluateMathExpression(document.getElementById("search").value)
.then(result => {
	if (result) {
	console.log('Result:', result);
	let fieldset = document.createElement("fieldset");

	let heading = document.createElement("h4");
	heading.innerHTML = "Math.js Calculator Api";
	heading.setAttribute("class", "links");
	heading.setAttribute("style", "margin: 2px; margin-top: 4px;");

	let iconDiv = document.createElement("div");
	iconDiv.setAttribute("style", "display: flex; color: #687485; margin: 4px;");

	let icon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
	icon.setAttribute("xmlns", "http://www.w3.org/2000/svg");
	icon.setAttribute("width", "24");
	icon.setAttribute("height", "24");
	icon.setAttribute("fill", "currentColor");
	icon.setAttribute("class", "bi bi-calculator");
	icon.setAttributeNS(null, "viewBox", "0 0 16 16");

	let iconPath = document.createElement("path");
	iconPath.setAttribute("d", "M12 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h8zM4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H4z");

	let iconPath2 = document.createElement("path");
	iconPath2.setAttribute("d", "M4 2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5v-2zm0 4a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-4z");
	
	let equation = document.createElement("p");
	equation.innerHTML = document.getElementById("search").value + " = ";
	equation.setAttribute("class", "links");
	equation.setAttribute("style", "display: flex; color: #687485; margin-left: 8px;");

	let answer = document.createElement("h3");
	answer.innerHTML = result;
	answer.setAttribute("class", "links");
	answer.setAttribute("style", "margin-left: 16px;");

	fieldset.appendChild(iconDiv);
	icon.appendChild(iconPath);
	icon.innerHTML += "\\n";
	icon.appendChild(iconPath2);
	icon.innerHTML += "\\n";
	iconDiv.appendChild(icon);
	iconDiv.appendChild(heading);
	fieldset.appendChild(equation);
	fieldset.appendChild(answer);

	let parentElement = document.getElementById("content");	
	parentElement.insertBefore(fieldset, parentElement.children[1]);
}});